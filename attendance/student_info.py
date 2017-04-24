import get_data
import login_credential
import string_functions


class Course:
    """
    Course class containing data like code, title, type and attendance of a course
    """

    def __init__(self, code, title, type, grade, names_list, attend=[]):
        """

        :param code:
        :param title:
        :param type:
        :param names_list: list of possible names of the course
        :param attend: pass 2 values corresponding to attended and total classes
        """
        self.course_code = code
        self.course_title = title
        self.subject_type = type
        self.names = names_list

        self.attendance = Attendance(attend[0], attend[1])

        if grade >= 9:
            self.attendance.minimum_percentage_required = None
        if self.subject_type == 'Lab Only' or 'Embedded Lab':
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

        self.attendance_percentage = float(self.attended_classes) / self.total_classes * 100

    def get_dict(self):
        q = dict()

        q['attended_classes'] = self.attended_classes
        q['total_classes'] = self.total_classes
        q['attendance_percentage'] = self.attendance_percentage

        return q

    def isDebarred(self, attendance_percentage=None):
        if attendance_percentage is None:
            attendance_percentage = self.attendance_percentage

        if self.minimum_percentage_required is None:
            return False

        if attendance_percentage < self.minimum_percentage_required:
            return True

        return False

    def attend_next_class(self, no_of_classes=1):
        new_percentage = float(self.attended_classes + no_of_classes * self.attendance_units) / \
                                (self.total_classes + no_of_classes * self.attendance_units) * 100

        return new_percentage

    def miss_next_class(self, no_of_classes=1):
        new_percentage = float(self.attended_classes) / (self.total_classes + no_of_classes
                                                         * self.attendance_units) * 100

        return new_percentage


class Student:
    """
    class containing data relating to courses and some personal info
    """

    def __init__(self):
        login_info = login_credential.LoginDetails()

        res = get_data.get_course_details(login_info)

        self.name = res['name']
        self.reg_no = res['reg_no']
        self.grade = res['academic_history']['history 2']['cgpa']

        self.courses = list()

        for course in res['courses']:
            c_code = course['course_code']
            c_title = course['course_title']
            c_type = course['subject_type']
            c_names = string_functions.get_names(course)

            a_tc = course['attendance']['total_classes']
            a_ac = course['attendance']['attended_classes']

            if a_tc == 0:   #prevent ZeroDivisionError
                continue

            temp = Course(c_code, c_title, c_type, self.grade, c_names, [a_ac, a_tc])
            self.courses.append(temp)

    def debug(self):
        print self.name
        print self.reg_no
        print self.grade
        print

        for i in self.courses:
            print i.course_code, '\t',
            print i.subject_type