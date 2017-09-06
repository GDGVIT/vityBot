from domains.db import find_DB


def best_match(query, intent):
    res = find_DB.find_match(query, intent)
    return res
