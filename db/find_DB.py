from pprint import pprint
from fuzzywuzzy import fuzz
import pymongo


conn = pymongo.MongoClient('mongodb://chatbot-learn:qwerty1234@ds135592.mlab.com:35592/chatbot-learn')
db = conn['chatbot-learn']
col = db.ques


def find_all(collection):
    for d in collection.find():
        yield d


def find_match(query):
    global col
    doc = None
    max = 0

    # for d in col.find():
    for d in find_all(col):
        ratio = fuzz.token_set_ratio(d['question'], query)

        if ratio > max:
            max = ratio
            doc = d

    del doc['_id']
    return doc


key = ['x_day', 'x_class', 'x_days']


def get_response(matched_dbdata):
    """

    :param matched_dbdata: the data returned from db from the find_match function
    :return: apt response as string
    """
    for i in key:
        if i in matched_dbdata['question']:
            # do stuff for calculation functions
            return False

    return matched_dbdata['answer']
