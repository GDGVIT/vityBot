from domains.db import find_DB

def best_match(query):
    res = find_DB.find_match(query)
    return res
