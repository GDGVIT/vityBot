def get_response(keyword, course):
    """
    process the response
    :param keyword: the keyword in the query
    :param course: course object
    :return: response  as string
    """

    if type(keyword) == list:
        if 'attendance' in keyword:
            n = keyword[1] if len(keyword) == 2 else 1
            s = course.attendance.attend_next_class(n)

            response = 'You will have an attendance of ' + '%.2f in ' % s + course.course_code

            return response

        elif 'debarred' in keyword:
            n = keyword[1] if len(keyword) == 2 else 1
            s = course.attendance.miss_next_class(n)

            response = 'You will have an attendance of ' + '%.2f in ' % s + course.course_code

            if course.attendance.isDebarred(s):
                response += '\nYou will be debarred'
            else:
                response += '\nYou will not be debarred'

            return response

    if keyword is 'attendance':
        s = course.attendance.attendance_percentage

        response = 'Your attendance in ' + course.course_code + ' is %.2f' % s

        return response

    elif keyword is 'debarred':
        if course.attendance.isDebarred():
            response = 'You are debarred from the course ' + course.course_code
        else:
            response = 'You are not debarred from the course ' + course.course_code

        return response
