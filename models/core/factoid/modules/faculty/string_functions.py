from fuzzywuzzy import fuzz

import json

import os

data = list()   # faculty data taken from output folder

# should be replaced with VIT API
# with open('db/output/data.json') as f:
with open(os.getcwd() + '/faculty/db/output/data.json') as f:
    data = json.load(f)


def find_match(query_string):
    """
    find the matching faculty object from the query string
    :param query_string:
    :return: faculty dictionary object
    """
    global data

    max_ratio = 0
    max_faculty = None

    for faculty in data:
        ratio = fuzz.token_set_ratio(faculty['name'], query_string)

        if ratio > max_ratio:
            max_ratio = ratio
            max_faculty = faculty

    return max_faculty if max_ratio > 40 else None


def get_keyword(query):
    """
    get keywords necessary for generating response
    :param query: query string
    """

    if ('room' in query) or ('cabin' in query):
        return 'room'

    email_keys = ['mail', 'email']

    for email in email_keys:
        if email in query:
            return 'email'

    open_hours_keys = ['meet', 'open', 'free']
    days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']

    for key in open_hours_keys:
        if key in query:
            for day in days:
                if day in query:
                    return ['open_hours', day]

            from datetime import datetime
            return ['open_hours', days[datetime.now().weekday()]]
