# script to test the interface

from attendance import get_data
from attendance import string_functions
from attendance import student_info
from attendance import handle_query
from db import find_DB

try:
    user = student_info.Student()

except get_data.InvalidCredentials as e:
    print e.message
    exit(1)
except get_data.LoginError as e:
    print e.message
    exit(1)

print

print 'Hi ' + user.name + '! What do you want me to do?'

print 'Q/q to quit\n'

while True:
    query = raw_input('>>').rstrip('?')
    if query == 'q':
        break

    # dbdoc = find_DB.find_match(query)
    # response = find_DB.get_response(dbdoc)
    #
    # course_reqd = string_functions.find_match(user.courses, query)
    #
    # if response and not course_reqd:
    #     print
    #     print response
    #     print
    #     continue
    #
    # print
    #
    # keyword = string_functions.get_keyword(query)
    #
    # response = handle_query.get_response(keyword, course_reqd, user)
    #
    # if response is None:
    #     print 'can\'t get you'
    # else:
    #     print response

    response = handle_query.process_query(user, query)

    print response
