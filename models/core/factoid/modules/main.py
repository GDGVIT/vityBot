# script to test the interface
import bot

from student_info import get_data
from attendance import string_functions
from student_info import student_info
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


print 'Hi ' + user.name + '! What do you want me to do?'

print 'Q/q to quit\n'

while True:
    query = raw_input('>>').rstrip('?')
    if query == 'q':
        break

    response = bot.chat(query)


    print response
