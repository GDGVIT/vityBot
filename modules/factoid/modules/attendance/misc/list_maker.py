import numpy as np
import codecs

# need to replace this text data and read from a database
# the database will store QA input from a website
# this website will be used to help management guys contribute to our
# dataset

# for file 1
with codecs.open("attendance1.txt", "r", "utf-8") as docs_file:
    sents = docs_file.readlines()

sents = [x.strip() for x in sents if len(x.strip()) > 0]

questions = []
answers = []

for index, sent in enumerate(sents):

    if index % 2 == 0:
        questions.append(sent)
    elif len(sent) > 0:
        answers.append(sent)

np.save('attendance_Q1.npy', questions)
np.save('attendance_A1.npy', answers)

# testing
questions = np.load('attendance_Q1.npy')
answers = np.load('attendance_A1.npy')
print(questions)
print(answers)
np.testing.assert_equal(len(questions), len(answers))


# for file 2
with codecs.open("attendance2.txt", "r", "utf-8") as docs_file:
    sents = docs_file.readlines()

sents = [x.strip() for x in sents if len(x.strip()) > 0]

questions = []
answers = []

for index, sent in enumerate(sents):

    if index % 2 == 0:
        questions.append(sent)
    elif len(sent) > 0:
        answers.append(sent)

np.save('attendance_Q2.npy', questions)
np.save('attendance_A2.npy', answers)

# testing
questions = np.load('attendance_Q2.npy')
answers = np.load('attendance_A2.npy')
print(questions)
print(answers)
np.testing.assert_equal(len(questions), len(answers))

