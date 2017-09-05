from domains import student_info
from domains.attendance import attendance
from domains.faculty import faculty
from domains.timetable import timetable

user = student_info.get_user()

print attendance('my attendance in cse', user)
print faculty('what is narayan  email', user)
print timetable('what is my next class', user)
'''

from domains import *

user  = student_info.get_user()
print = attendance.attendance(
'''
