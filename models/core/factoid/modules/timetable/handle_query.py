import string_functions
from datetime import datetime


def get_response(keyword, user):
    """

    :param keyword: keywords from query
    :param user: student object
    :return: response as string
    """
    weekdays = ['monday', 'tuesday', 'wednesday',
                'thursday', 'friday']
    course_index = 0
    time_index = 1

    if keyword[0] == 'classes':
        if keyword[1] == 'today':
            day = datetime.now().weekday()
            day = weekdays[day]

            if not day:
                return 'You don\'t have any classes that day'

            classes = user.timetable.all_classes(day)
            response = 'you have '

            for i in classes:
                response += i[course_index].course_code + ' at ' + \
                            str(i[time_index][0].hour) + ':' +\
                            str(i[time_index][0].minute) + ', '

            return response

        elif keyword[1] == 'tomorrow':
            day = datetime.now().weekday() + 1
            day = weekdays[day]

            if not day:
                return 'You don\'t have any classes that day'

            classes = user.timetable.all_classes(day)
            response = 'you have '

            for i in classes:
                response += i[course_index].course_code + ' at ' + \
                            str(i[time_index][0].hour) + ':' + \
                            str(i[time_index][0].minute) + ', '

            return response

        elif keyword[1] == 'end':
            day = datetime.now().weekday()
            day = weekdays[day]

            if not day:
                return 'You don\'t have any classes that day'

            classes = user.timetable.all_classes(day)
            end_time = classes[-1][time_index][1]
            response = 'your day ends at ' + str(end_time.hour) + \
                       ':' + str(end_time.minute)

            return response

    elif keyword[0] == 'class':
        if keyword[1] == 'current':
            # time = datetime.now()
            day = datetime(2017, 8, 24, 14)

            if not day:
                return 'You don\'t have any classes that day'

            time = day.time()

            cls = user.timetable.current_class(time)
            response = 'your current class is ' + cls.course_code

            return response

        elif keyword[1] == 'next':
            # time = datetime.now()
            day = datetime(2017, 8, 24, 14)

            if not day:
                return 'You don\'t have any classes that day'

            time = day.time()

            cls = user.timetable.next_class(time)
            response = 'your next class is ' + cls[course_index].course_code\
                       + ' at ' + str(cls[time_index][0].hour) + ':'\
                       + str(cls[time_index][0].minute)

            return response


def process_query(user, query):
    keyword = string_functions.get_keyword(query)
    response = get_response(keyword, user)

    return response
