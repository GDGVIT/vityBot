from domains import student_info
from domains.attendance import attendance
from domains.faculty import faculty
from domains.timetable import timetable
import best_match

user = student_info.get_user()

print attendance('what is my attendance in mat2002 lab', user)
