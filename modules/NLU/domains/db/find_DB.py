import env
import sys

from .. import attendance
from .. import faculty
from ..timetable import handle_query
from fuzzywuzzy import fuzz
import pymongo

host = env.host
conn = pymongo.MongoClient(host)
db = conn['vitybot']
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
    return doc['answer']


key = ['x_day', 'x_class', 'x_days', 'x_classes']


def get_response(query, intent, user):
    """
    :return: apt response as string
    """

    # matched_dbdata = find_match(query)

    if intent == 'faculty-calculation':
        response = faculty.handle_query.process_query(query)
        if response:
            return response

    if intent == 'attendance-calculation':
        response = attendance.handle_query.process_query(user, query)
        if response:
            return response

    if intent == 'timetable-calculation':
        response = handle_query.process_query(user, query)
        if response:
            return response
