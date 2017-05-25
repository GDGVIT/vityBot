from fuzzywuzzy import fuzz


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

    max_out = 0
    max_course = None

    for course in course_list:
        if 'lab' not in query_string.lower():
            if course.subject_type == 'Embedded Lab':
                continue
        else:
            if course.subject_type == 'Embedded Theory':
                continue

        #print course.course_title

        max_in = 0

        for name in course.names:
            ratio = fuzz.token_set_ratio(name, query_string)

            if ratio > max_in:
                max_in = ratio

        if max_out < max_in:
            max_out = max_in
            max_course = course

    return max_course


def get_keyword(query):
    """
    get keywords necessary for generating response
    :param query:
    :return:
    """

    #words and their synonyms
    attend = ['go', 'attend']
    miss = ['miss', 'skip', 'don\'t', 'debarred']

    # code to check if queries regarding attendance over a few classes are asked
    li = list()
    flag = False
    for s in query.split(' '):
        if s.isdigit():         #push no of classes if it exist to index 1
            if flag:
                li.append(s)
                break

        if s in attend:
            if not flag:
                li.append('attendance')
                flag = True

        if s in miss:
            if not flag:
                li.append('debarred')
                flag = True

    if len(li) == 1 or len(li) == 2:
        return li

    if 'attendance' in query:
        return 'attendance'
    elif 'debarred' in query:
        return 'debarred'
