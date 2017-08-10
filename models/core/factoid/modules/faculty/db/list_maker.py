import numpy as np
import codecs

# script adds test data in to a local repo

with codecs.open("questions.txt", "r", "utf-8") as docs_file:
    sents = docs_file.readlines()

sents = [x.strip() for x in sents if len(x.strip()) > 0]

questions = []
answers = []

for index, sent in enumerate(sents):

    if index % 2 == 0:
        questions.append(sent)
    elif len(sent) > 0:
        answers.append(sent)

np.save('faculty_Q.npy', questions)
np.save('faculty_A.npy', answers)

# testing
questions = np.load('faculty_Q.npy')
answers = np.load('faculty_A.npy')
print(questions)
print(answers)
np.testing.assert_equal(len(questions), len(answers))
