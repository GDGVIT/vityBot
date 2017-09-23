from vityBot.modules.NLU.domains.faculty import handle_query


def faculty(query, user):
    try:
        res = handle_query.process_query(query)
    except Exception as e:
        print(e)
        # log to website
        res = "Can't get you"

    return res
