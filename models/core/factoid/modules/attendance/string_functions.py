from fuzzywuzzy import fuzz
import json
import day_functions


def get_names(course_dict):
    """
    get all possible names for a course
    :param course_dict: dictionary of course info
    :return: list of names
    """
    li = list()

    li.append(course_dict['course_code'])
    li.append(course_dict['course_title'])

    name = str()
    for i in course_dict['course_title'].split():
        if i[0].isupper():
            name += i[0]

    li.append(name)

    return li


def find_match(course_list, query_string):
    """
    find the most matching course for a given name and return the course
    :param course_list: list of courses
    :param query_string: query of the user
    :return: course object
    """

    max_out = 0  # the max ratio among the courses
    max_course = None

    for course in course_list:
        if 'lab' not in query_string.lower():
            if course.subject_type == 'Embedded Lab':
                continue
        else:
            if course.subject_type == 'Embedded Theory':
                continue

        max_in = 0  # the max ratio among different names of the course

        for name in course.names:
            ratio = fuzz.token_set_ratio(name, query_string)

            if ratio > max_in:
                max_in = ratio

        if max_out < max_in:
            max_out = max_in
            max_course = course

    return max_course if max_out > 50 else None


def get_days(slots):
    """
    get the days from the slots
    :param slots:list of slots
    """

    with open('attendance/tt.json') as file_obj:
        table = json.load(file_obj)

    days = list()

    for slot in slots:
        for day in table.keys():
            if slot in table[day]:
                if day not in days:
                    days.append(day)

    return days


def get_keyword(query):
    """
    get keywords necessary for generating response
    :param query:
    :return:
    """

    # verbs and their synonyms
    attend = ['go', 'attend']
    miss = ['miss', 'skip', 'don\'t', 'bunk']

    # code to check queries regarding attendance over a few classes
    li = list()
    flag = False  # flag for checking if digit/day follows
    #  the keywords reqd(attend/miss) in li

    for s in query.split(' '):
        if s.isdigit():  # push no of classes if it exist to index 1
            if flag:
                li.append(int(s))
                break

        elif s in day_functions.weekdays:
            if flag:
                li.append(s)  # push the week of day to index 1 of li
                break

        if s in miss:
            if not flag:
                li.append('debarred')
                flag = True

        if s in attend:
            if not flag:
                li.append('attendance')
                flag = True

    if 'how' in query:
        li.append('how')

    if len(li) == 1 or len(li) == 2:
        # list can't have values other than 1 and 2
        return li

    if 'attendance' in query:
        return 'attendance'
    elif 'debarred' in query:
        return 'debarred'
