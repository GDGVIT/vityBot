"""
the script adds all data from the .npy files to the DB
"""


import pymongo
import numpy as np
import json

"""
writes list of question and answer from .npys to DB
"""

conn = pymongo.MongoClient("some link")  # host link here
db = conn['chatbot-learn']
coll = db.ques

list_docs = list()

questions = np.load('tt_Q.npy')
answers = np.load('tt_A.npy')

for i in range(len(questions)):
    doc = dict()

    doc['type'] = 'timetable-calculation'
    doc['question'] = questions[i]
    doc['answer'] = answers[i]

    list_docs.append(doc)

    # with open('db.json', 'a') as f:
    #     json.dump(doc, f, indent=4)
    #     f.write('\n')

    del doc

# coll.insert_many(list_docs)
