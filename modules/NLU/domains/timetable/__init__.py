from vityBot.modules.NLU.domains.timetable import handle_query


def timetable(query, user):
    try:
        res = handle_query.process_query(user, query)
    except Exception as e:
        print(e)
        # log to website

        res = "can't get you!"

    return res
