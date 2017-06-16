import pymongo
import numpy as np

"""
writes list of question and answer from .npys to DB
"""

conn = pymongo.MongoClient('localhost', 27017)
db = conn.vityBot
coll = db.attendance

questions = np.load('attendance_Q.npy')
answers = np.load('attendance_A.npy')

list_docs = list()

for i in range(len(questions)):
    doc = dict()

    doc['question'] = questions[i]
    doc['answer'] = answers[i]

    list_docs.append(doc)
    del doc

#clear currrent collection
coll.drop()

coll.insert_many(list_docs)
