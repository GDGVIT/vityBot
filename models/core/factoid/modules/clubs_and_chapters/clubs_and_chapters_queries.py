from pymongo import MongoClient
client = MongoClient()
client = MongoClient('localhost', 27017)
db = client['clubs_and_chapters']
collection = db['clubs_and_chapters_data']

out_list = []
prior_list = []


def clubs_and_chapters(query, token):
    flag = False
    confidence = 0.80

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

    # CLubs and chapters according to ratings
    if ("best" in query) or ("top" in query):
        flag = True
        if (("club" in query) and ("chapter" in query)) or (("club" not in query) and ("chapter" not in query)):
            for post in db.posts.find().sort("rating", -1):
                check_priority(post)
        elif ("club" in query):
            for post in db.posts.find({"clb_or_chap": 'club'}).sort("rating", -1):
                check_priority(post)
        elif ("chapter" in query):
            for post in db.posts.find({"clb_or_chap": 'chapter'}).sort("rating", -1):
                check_priority(post)

    # Data about all clubs and chapters depending on name in query
    if not flag:
        for post in db.posts.find({}):
            if (post["name"].lower() in query) or (post["abbrivation"].lower() in query) and (post["abbrivation"]!=''):
                flag = True
                check_priority(post)

    # Data about all the clubs and chapters of same type (IEEE,Arts etc.)
    if not flag:
        for post in db.posts.find({}):
            if (post["type"].lower() in query) or check_tags(post):
                flag = True
                check_priority(post)

    # Data for all clubs or all chapters
    if not flag:
        if "club" in query:
            for post in db.posts.find({"clb_or_chap": 'club'}):
                if post["clb_or_chap"].lower() in query:
                    flag = True
                    check_priority(post)
        elif "chapter" in query:
            for post in db.posts.find({"clb_or_chap": 'chapter'}):
                if post["clb_or_chap"].lower() in query:
                    flag = True
                    check_priority(post)

    if len(prior_list):
        return(prior_list, confidence)
    return(out_list, confidence)
