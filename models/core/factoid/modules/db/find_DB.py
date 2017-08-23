import attendance
import faculty
import dblink

from fuzzywuzzy import fuzz
import pymongo


conn = pymongo.MongoClient(dblink.host)
db = conn['chatbot-learn']
col = db.ques


def find_all(collection):
    for d in collection.find():
        yield d


def find_match(query):
    global col
    doc = None
    max_ratio = 0

    for d in find_all(col):
        ratio = fuzz.token_set_ratio(d['question'], query)

        if ratio > max_ratio:
            max_ratio = ratio
            doc = d

    del doc['_id']
    return doc


key = ['x_day', 'x_class', 'x_days', 'x_classes']


def get_response(query, user):
    """
    :return: apt response as string
    """

    matched_dbdata = find_match(query)

    if matched_dbdata['type'] == 'faculty-calculation':
        response = faculty.handle_query.process_query(query)
        if response:
            return response

    if matched_dbdata['type'] == 'attendance-calculation':
        response = attendance.handle_query.process_query(user, query)
        if response:
            return response

    return matched_dbdata['answer']

