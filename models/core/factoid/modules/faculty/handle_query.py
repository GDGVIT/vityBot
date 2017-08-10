def get_response(keyword, faculty):
    """
    process the response
    :param faculty: faculty dictionary object
    :return:
    """

    response = str()

    if type(keyword) == list:
        # if keyword is list - query relating to open hours
        # index 1 = day of the week

        day = keyword[1][:3].capitalize()   # convert day to apt format

        for i in faculty['open_hours']:
            if i['day'] == day:
                response += 'open hours of ' + faculty['name'] + ' on '
                response += keyword[1] + ' : '
                response += i['start_time'] + ' to ' + i['end_time'] + '\n'

                return response

        # if data not present
        if len(faculty['open_hours']) == 0:
            return "can't get requested data\n"

        # if not free that day
        response += faculty['name'] + ' is not free on '
        response += keyword[1] + '\n'
        return response


    if keyword == 'room':
        response += faculty['name'] + "'s room : "
        response += faculty['room'] + '\n'

        return response

    if keyword == 'email':
        response += faculty['name'] + "'s email id : "
        response += faculty['email'] + '\n'

        return response
