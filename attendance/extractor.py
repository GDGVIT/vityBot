subjects = {'DLM': ['digital', 'dlm', 'microprocessors'], 'DSA': ['dsa', 'data', 'algorithms'],
            'PHY': ['phy', 'physics'], 'MAT': ['mat', 'maths', 'math' 'ade', 'applications']}


def intersection_list(li1, li2):
    """
    checks for intersection of elements in two list
    and returns the first matching element present in both lists
    """
    for i in li1:
        if i in li2:
            return i

    return ''


def intersection_dict(li, subs_dict):
    """
    func finds if any value in a list is present in the value lists of a dict
    if true it returns the key
    """
    for i in subs_dict.keys():
        if intersection_list(li, subs_dict[i]) != '':
            return i

    return ''


def extractKeyWords(li):
    """
    function extracts keywords necessary for querying from the input string
    """
    global subjects
    keywords = list()

    for i in li:
        if i == 'attendance':
            keywords.append('attendance')
        elif i == 'debarred':
            keywords.append('debarred')
        elif i == 'average':
            keywords.append('attendance')

    subs = intersection_dict(li, subjects)
    if subs != '':
        keywords.append(subs)

    return keywords
