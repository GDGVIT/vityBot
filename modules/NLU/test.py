from domains import student_info
from domains import attendance
from domains import faculty
from domains import timetable

user = student_info.get_user()

print attendance.attendance('my attendance in cse', user)
print faculty.faculty('what is narayan  email', user)
print timetable.timetable('what is my next class', user)