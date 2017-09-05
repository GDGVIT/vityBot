from pymongo import MongoClient
from fuzzywuzzy import fuzz
client = MongoClient()
client = MongoClient('localhost', 27017)
db = client['clubs_and_chapters_data']
db_q = client['clubs_and_chapters_questions']

out_list = []
prior_list = []


def clubs_and_chapters(query, token):
    flag = False
    confidence = 0

    def check_tags(post):
        for tag in post["tags"]:
                if tag.lower() in query:
                    return(True)
        return(False)

    def check_priority(post):
        if check_tags(post):
            prior_list.append(post)
        if not len(prior_list):
            out_list.append(post)

    def calculate_confidence(typ):
        all_c = []
        for i in db_q.posts.find({"type": str(typ)}):
            all_c.append(fuzz.token_sort_ratio(i["question"].lower(), query))
        return(max(all_c))

    # Clubs and chapters according to ratings
    if ("best" in query) or ("top" in query):
        flag = True
        if (("club" in query) and ("chapter" in query)) \
                or (("club" not in query) and ("chapter" not in query)):
            for post in db.posts.find().sort("rating", -1):
                check_priority(post)
        elif ("club" in query):
            for post in db.posts.find({"clb_or_chap": 'club'}) \
                    .sort("rating", -1):
                check_priority(post)
        elif ("chapter" in query):
            for post in db.posts.find({"clb_or_chap": 'chapter'}) \
                    .sort("rating", -1):
                check_priority(post)
        if flag:
            confidence = calculate_confidence(1)

    # Data about all clubs and chapters depending on name in query
    if not flag:
        for post in db.posts.find({}):
            if (post["name"].lower() in query) or \
                    (post["abbrivation"].lower() in query) and \
                    (post["abbrivation"] != ''):
                flag = True
                check_priority(post)
        if flag:
            confidence = calculate_confidence(2)

    # Data about all the clubs and chapters of same type (IEEE,Arts etc.)
    if not flag:
        for post in db.posts.find({}):
            if (post["type"].lower() in query) or check_tags(post):
                flag = True
                check_priority(post)
        if flag:
            confidence = calculate_confidence(2)

    # Data for all clubs or all chapters
    if not flag:
        if "club" in query:
            for post in db.posts.find({"clb_or_chap": 'club'}):
                if post["clb_or_chap"].lower() in query:
                    flag = True
                    check_priority(post)
        if "chapter" in query:
            for post in db.posts.find({"clb_or_chap": 'chapter'}):
                if post["clb_or_chap"].lower() in query:
                    flag = True
                    check_priority(post)
        if flag:
            confidence = calculate_confidence(3)

    if len(prior_list):
        return(prior_list, confidence)
    return(out_list, confidence)
