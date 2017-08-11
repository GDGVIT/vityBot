"""
assumptions:
1. no course can have 2 labs in the same day
2. labs always come in pairs
"""
from datetime import time
import json


def generate(course_list):
    """
    generate time table from list of course objects
    :param course_list:
    :return: dict with weekdays and corresponding classes with time interval
    """

    def get_time(index, c_type):
        """
        get
        :param index: index of cell from the table data
        :param c_type: type of course
        :return: time interval of the class in list of datetime.time obj
        """
        if c_type == 'theory':
            h = 8 + index
            m = 0
            from_time = time(h, m)
            m = 50
            to_time = time(h, m)

            return [from_time, to_time]

        elif c_type == 'lab':
            if index == 4 or index == 10:
                h = 8 + index - 1
                m = 50
                from_time = time(h, m)
                h = 8 + index + 1
                m = 30
                to_time = time(h, m)

                return [from_time, to_time]

            elif index == 12:
                h = 8 + index - 1
                m = 31
                from_time = time(h, m)
                h = 8 + index + 1
                m = 10
                to_time = time(h, m)

                return [from_time, to_time]

            else:
                h = 8 + index
                m = 0
                from_time = time(h, m)
                h = 8 + index + 1
                m = 40
                to_time = time(h, m)

                return [from_time, to_time]

    output = dict(monday=[], tuesday=[], wednesday=[], thursday=[], friday=[])

    with open('student_info/tt.json') as f:
        tt = json.load(f)

    days = tt.keys()
    total_cols = 14

    for c in course_list:
        if c.subject_type == 'Lab Only' or \
                        c.subject_type == 'Embedded Lab':
            for slot in c.slots[::2]:  # take 2 labs together
                for day in days:
                    i = 0

                    while i < total_cols:
                        if slot == tt[day][i][1]:
                            val = [c, get_time(i, 'lab')]
                            output[day].append(val)

                        i += 1

        else:
            for slot in c.slots:
                for day in days:
                    i = 0

                    while i < total_cols:
                        if tt[day][i][0]:
                            if slot == tt[day][i][0]:
                                val = [c, get_time(i, 'theory')]
                                output[day].append(val)

                        i += 1

    return output
