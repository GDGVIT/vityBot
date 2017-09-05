import get_data
import login_credentials
from  ..attendance import string_functions
import timetable

import math
import json
import os
from datetime import time
from datetime import datetime


class Course:
    """
    Course class containing data like code, title, type and
     attendance of a course
    """

    def __init__(self, code, title, subject_type, grade, slots,
                 names_list, days_list, attend):
        """
        :param grade: cgpa, reqd to get min percent of the student
        :param names_list: list of possible names of the course
        :param days_list: list of days where the classes are conducted
        :param attend: pass list of 2 values - attended and total classes
        """
        self.course_code = code
        self.course_title = title
        self.subject_type = subject_type
        self.names = names_list
        self.days = days_list
        self.slots = slots

        self.attendance = Attendance(attend[0], attend[1])

        if grade >= 9:
            self.attendance.minimum_percentage_required = 0
        if self.subject_type == 'Lab Only' or \
           self.subject_type == 'Embedded Lab':
            self.attendance.attendance_units = 2

    def get_dict(self):
        d = dict()
        d['course_code'] = self.course_code
        d['course_title'] = self.course_title
        d['subject_type'] = self.subject_type

        d['attendance'] = self.attendance.get_dict()

        return d


class Attendance:
    """
    attendance class containing data like total and attended classes
    and attendance percentage of a course.
    methods relating to attendance.
    """
    minimum_percentage_required = 75
    attendance_units = 1

    def __init__(self, attended, total):
        self.attended_classes = attended
        self.total_classes = total

        self.attendance_percentage = int(math.ceil(
            float(self.attended_classes) / self.total_classes * 100))

    def get_dict(self):
        q = dict()

        q['attended_classes'] = self.attended_classes
        q['total_classes'] = self.total_classes
        q['attendance_percentage'] = self.attendance_percentage

        return q

    def is_debarred(self, attendance_percentage=None):
        if attendance_percentage is None:
            attendance_percentage = self.attendance_percentage

        if self.minimum_percentage_required is None:
            return False

        if attendance_percentage < self.minimum_percentage_required:
            return True

        return False

    def attend_next_class(self, no_of_classes=1):
        new_percentage = math.ceil(float(
            self.attended_classes + no_of_classes * self.attendance_units) /
                                   (self.total_classes + no_of_classes *
                                    self.attendance_units) * 100)

        return int(new_percentage)

    def miss_next_class(self, no_of_classes=1):
        new_percentage = math.ceil(
            float(self.attended_classes) /
            (self.total_classes + no_of_classes *
             self.attendance_units) * 100)

        return int(new_percentage)

    def miss_class_on(self, no_of_classes):
        """
        percentage if missed nth class from today
        :param no_of_classes:(n)
        """
        new_percentage = math.ceil(float(self.attended_classes +
                                   (no_of_classes - 1) *
                                         self.attendance_units) /
                                   (self.total_classes + no_of_classes *
                                    self.attendance_units) * 100)

        return int(new_percentage)


course = 0
duration = 1


class Timetable:
    """
    contains the timetable and some handy methods

    """

    def __init__(self, course_list):
        self.tt = timetable.generate(course_list)

    def show(self):
        days = self.tt.keys()
        out = dict()

        for day in days:
            out[day] = []
            for i in self.tt[day]:
                out[day].append([i[course].course_code, i[duration]])

        from pprint import pprint
        pprint(out)

    @staticmethod
    def _is_between(check_time, start_time, end_time):
        """
        check if a given time is between an interval
        :param check_time: datetime.time obj
        :param start_time: datetime.time obj
        :param end_time: datetime.time obj
        :return:
        """
        if start_time.hour < check_time.hour < end_time.hour:
            return True
        elif check_time.hour == start_time.hour and check_time.hour < \
                end_time.hour:
            return check_time.minute >= start_time.minute
        elif check_time.hour > start_time.hour and check_time.hour == \
                end_time.hour:
            return check_time.minute <= end_time.minute
        elif check_time.hour == start_time.hour and check_time.hour == \
                end_time.hour:
            return start_time.minute <= check_time.minute <= end_time.minute
        else:
            return False

    @staticmethod
    def _is_before(check_time, start_time):
        """
        check if check_time is before start_time
        :param check_time: datetime.time obj
        :param start_time: datetime.time obj
        :return:
        """
        if check_time.hour < start_time.hour:
            return True
        elif check_time.hour == start_time.hour:
            return check_time.minute < start_time.minute
        else:
            return False

    def current_class(self, time):
        """
        get the class in a given time
        :param time: datetime.time object
        :return: course
        """
        day = datetime.now().weekday()
        weekdays = ['monday', 'tuesday', 'wednesday',
                    'thursday', 'friday']
        courses = self.all_classes(weekdays[day])

        for c in courses:
            if self._is_between(time, *c[duration]):
                return c[course]
        return None

    def next_class(self, time):
        """
        get the class next to a given time
        :param time: datetime.time object
        :return: [course, course time]
        """
        day = datetime.now().weekday()
        weekdays = ['monday', 'tuesday', 'wednesday',
                    'thursday', 'friday']
        courses = self.all_classes(weekdays[day])

        for c in courses:
            if self._is_before(time, c[duration][0]):
                # return the first class that follows given time
                return c
        # no class after given time
        return None

    def all_classes(self, weekday):
        """
        all the classes in a given weekday
        :return: [[course, time], ...]
        """
        weekdays = ['monday', 'tuesday', 'wednesday',
                    'thursday', 'friday']

        if weekday not in weekdays:
            return None
        # sort by time before return
        out = self.tt[weekday]
        out.sort(key=lambda x: x[1][0].hour)
        return out


class Student:
    """
    class containing data relating to courses and some personal info
    """

    def __init__(self):
        # login_info = login_credential.LoginDetails()
        #
        # res = get_data.get_course_details(login_info)

        with open(os.getcwd() + '/domains/student_info/ffcs.json') as f:  # temp json file
            res = json.load(f)

        self.name = res['name']
        self.reg_no = res['reg_no']
        self.grade = res['academic_history']['history 2']['cgpa']

        self.courses = list()

        for course in res['courses']:
            c_code = course['course_code']
            c_title = course['course_title']
            c_type = course['subject_type']
            c_names = string_functions.get_names(course)
            c_slots = course['slot'].split('+')
            c_days = string_functions.get_days(c_slots)

            if c_type == 'Embedded Lab' or c_type == 'Lab Only':
                c_code += 'L'

            a_tc = course['attendance']['total_classes']
            a_ac = course['attendance']['attended_classes']

            if a_tc == 0:  # prevent ZeroDivisionError
                continue

            temp = Course(c_code, c_title, c_type, self.grade, c_slots,
                          c_names, c_days, [a_ac, a_tc])
            self.courses.append(temp)

        self.timetable = Timetable(self.courses)
