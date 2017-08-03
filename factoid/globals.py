"""
 this file imports all the other modules which answer
 factoid based questions
 put all your modules inside the factoid folder

    module schema:
        input: question, tokens(optional)
        output: (confidence, answer)
    Steps to add your own module:
    1. Make a new folder in this folder by your module name with
    2. Write a module.py in this folder which follows above
       schema along with a __init__.py which can be left empty.
    3. import you module here.
    4. import a list of keywords you think are unique to your module
    5. add your module name, keywords list as key,value pairs in the
       keywords dict

    Guidelines for all modules:
    1. use your own collection of QAs
    2. use your own question embeddings if you are using deep_match

"""


# these are dummy functions and lists
def attendance(question, tokens=None):
    return (0.8, 'got the question')


def clubs_chapters(question, tokens=None):
    return (0.8, 'got the question')

att_kw_list = ['bunk', 'attendance']
clubs_kw_list = ['club', 'chapter']


keywords = dict(
                attendance=att_kw_list,
                clubs_chapters=clubs_kw_list
)
modules = keywords.keys()
