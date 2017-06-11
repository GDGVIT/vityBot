import pymongo
import numpy as np

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

coll.insert_many(list_docs)
