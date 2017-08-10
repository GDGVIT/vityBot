from datetime import datetime

weekdays = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']


def classes_between(day, course):
    """
    no of classes in between today and a given day for a course
    :param day: day in string
    """
    count = 0
    day = weekdays.index(day)           # convert day in string to integer
    today = datetime.today().weekday()
    i = today

    if i == day:
        if weekdays[i] in course.days:
            count += 1
            i = (i + 1) % 7

    while i != day:
        if weekdays[i] in course.days:
            count += 1
        i = (i + 1) % 7

    if weekdays[i] in course.days:
        count += 1

    return count

