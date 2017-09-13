import vityBot.modules.NLU.domains.attendance.handle_query


def attendance(query, user):
    return handle_query.process_query(user, query)
