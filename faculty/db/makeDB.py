"""
the script adds all data from the .npy files to the DB
"""


import pymongo
import numpy as np
import json

"""
writes list of question and answer from .npys to DB
"""

conn = pymongo.MongoClient('localhost', 27017)
db = conn['vityBot']
coll = db.faculty

list_docs = list()

# type 1

questions = np.load('faculty_Q.npy')
answers = np.load('faculty_A.npy')

for i in range(len(questions)):
    doc = dict()

    doc['question'] = questions[i]
    doc['answer'] = answers[i]

    list_docs.append(doc)

    del doc

coll.drop()
coll.insert_many(list_docs)
