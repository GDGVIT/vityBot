"""
the script adds all data from the .npy files to the DB
"""


import pymongo
import numpy as np
import json

"""
writes list of question and answer from .npys to DB
"""

conn = pymongo.MongoClient('mongodb://chatbot-learn:qwerty1234@ds135592.mlab.com:35592/chatbot-learn')
db = conn['chatbot-learn']
coll = db.ques

list_docs = list()

# type 1

f = open('testjsonfolder/db1.json', 'a')
questions = np.load('attendance_Q1.npy')
answers = np.load('attendance_A1.npy')

for i in range(len(questions)):
    doc = dict()

    doc['question'] = questions[i].rstrip('?')
    doc['answer'] = answers[i]
    doc['submitted by'] = 'subham'
    doc['type'] = 'attendance'

    list_docs.append(doc)

    json.dump(doc, f, indent=4)
    f.write('\n')
    del doc


# type 2

f = open('testjsonfolder/db2.json', 'a')
questions = np.load('attendance_Q2.npy')
answers = np.load('attendance_A2.npy')

for i in range(len(questions)):
    doc = dict()

    doc['question'] = questions[i].rstrip('?')
    doc['answer'] = answers[i]
    doc['submitted by'] = 'subham'
    doc['type'] = 'attendance-calculation'

    list_docs.append(doc)

    json.dump(doc, f, indent=4)
    f.write('\n')
    del doc

# coll.insert_many(list_docs)