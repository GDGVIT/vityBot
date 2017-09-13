from vityBot.modules.NLU.domains.db import env

from fuzzywuzzy import fuzz
import pymongo

host = env.host
conn = pymongo.MongoClient(host)
db = conn['vitybot']
col = db['common_examples']


def find_match(query, intent):
    global col
    doc = None
    max_ratio = 0

    for d in col.find({"intent": intent}):
        ratio = fuzz.token_set_ratio(d['text'], query)

        if ratio > max_ratio:
            max_ratio = ratio
            doc = d

    del doc['_id']
    return doc['answer']
