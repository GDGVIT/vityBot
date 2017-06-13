import get_data
import student_info
import string_functions
import handle_query

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

    course_reqd = string_functions.find_match(user.courses, query)

    print

    keyword = string_functions.get_keyword(query)

    response = handle_query.get_response(keyword, course_reqd, user)

    if response is None:
        print 'can\'t get you'
    else:
        print response
