from vityBot.modules.NLU.domains.attendance import day_functions
from vityBot.modules.NLU.domains.attendance import string_functions


def get_response(keyword, course, user):
    """
    process the response
    :param keyword: the keyword in the query
    :param course: course object - found from query
    :param user: student object
    :return: response  as string
    """

    if not course:
        if type(keyword) == list:
            if 'debarred' in keyword and type(keyword[1]) == str:
                # if index 1 is a day of the week
                """
                queries relating to missing all classes in a day
                """

                day = keyword[1]
                li = list()  # list containing courses on that day

                for c in user.courses:
                    if day in c.days:
                        li.append(c)

                res_list = list()
                response = 'attendance in each courses: '

                for c in li:
                    no_of_classes = day_functions.classes_between(day, c)
                    s = c.attendance.miss_class_on(no_of_classes)
                    response += c.course_code + ' ' + str(s) + ', '

                    if c.attendance.is_debarred(s):
                        res_list.append(c)

                if len(res_list):
                    response += ', you will be debarred in '

                    for c in res_list:
                        response += c.course_code + ', '
                else:
                    response += ', you won\'t be debarred in any courses'

                return response

        li = list()

        if 'attendance' in keyword:
            for c in user.courses:
                li.append(str(c.course_code) + ' ' +
                          str(c.attendance.attendance_percentage))

            response = 'your attendance: '
            for i in li:
                response += i + ' '

            return response

        elif 'debarred' in keyword:
            li = list()

            for c in user.courses:
                if c.attendance.is_debarred():
                    li.append('{0} with {1}'.format(
                        str(c.course_code),
                        str(c.attendance.attendance_percentage)))

            if len(li) == 0:
                response = 'you are not debarred in any course'
            else:
                response = 'you are debarred in '
                for i in li:
                    response += i + ' '

            return response

    if type(keyword) == list:
        if 'attendance' in keyword:
            if len(keyword) == 1 or type(keyword[1]) == int:
                # if index 1 is no. of classes
                n = keyword[1] if len(keyword) == 2 else 1
                s = course.attendance.attend_next_class(n)

                response = 'You will have an attendance of ' \
                           + '%d in ' % s + course.course_code

                return response

            elif type(keyword[1]) == str:  # if index 1 is a day of the week
                if keyword[1] is 'how':
                    # questions like 'how many more classes to attend
                    cnt = 0

                    while course.attendance.is_debarred(        # !BUG BUG BUG
                            course.attendance.attend_next_class(cnt)):
                        cnt += 1

                    if cnt:
                        response = 'You have to attend %d more class(es)' % cnt
                    else:
                        response = 'You are not debarred'
                    return response

                else:
                    day = keyword[1]
                    if day not in course.days:
                        return 'You don\'t have ' + course.course_code + \
                               ' classes that day'

                    no_of_classes = day_functions.classes_between(day, course)
                    s = course.attendance.attend_next_class(no_of_classes)

                    response = 'You will have an attendance of ' + \
                               '%d in ' % s + course.course_code

                    return response

        elif 'debarred' in keyword:
            if len(keyword) == 1 or type(keyword[1]) == int:
                # if index 1 is no. of classes
                n = keyword[1] if len(keyword) == 2 else 1
                s = course.attendance.miss_next_class(n)

                response = 'You will have an attendance of ' + \
                           '%d in ' % s + course.course_code

                if course.attendance.is_debarred(s):
                    response += ', You will be debarred'
                else:
                    response += ', You will not be debarred'

                return response

            elif type(keyword[1]) == str:  # if index 1 is a day of the week
                if keyword[1] is 'how':
                    # questions like 'how many more classes can i miss'
                    cnt = 0

                    while not course.attendance.is_debarred(
                            course.attendance.miss_next_class(cnt)):
                        cnt += 1

                    cnt -= 1

                    if cnt > 0:
                        response = 'You can miss %d class(es)' % cnt \
                                   + ' in %s' % course.course_code
                    else:
                        response = 'You can\'t miss any class' + \
                                   ' in %s' % course.course_code

                    return response

                else:
                    day = keyword[1]
                    if day not in course.days:
                        return 'You don\'t have ' + course.course_code + \
                               ' classes that day'

                    no_of_classes = day_functions.classes_between(day, course)
                    s = course.attendance.miss_class_on(no_of_classes)

                    response = 'You will have an attendance of ' + \
                               '%d in ' % s + course.course_code

                    if course.attendance.is_debarred(s):
                        response += ', You will be debarred'
                    else:
                        response += ', You will not be debarred'

                    return response

    # if keyword is not a list
    if keyword is 'attendance':
        s = course.attendance.attendance_percentage

        response = 'Your attendance in ' + course.course_code + ' is %d' % s

        return response

    elif keyword is 'debarred':
        if course.attendance.is_debarred():
            response = 'You are debarred from the course ' \
                       + course.course_code
        else:
            response = 'You are not debarred from the course ' \
                       + course.course_code

        return response


def process_query(user, query):
    course_reqd = string_functions.find_match(user.courses, query)
    # if not course_reqd:
    #     return None

    keyword = string_functions.get_keyword(query)
    response = get_response(keyword, course_reqd, user)

    return response
