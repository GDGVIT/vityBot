import vityBot.modules.NLU.domains.timetable.handle_query

def timetable(query, user):
	return handle_query.process_query(user, query)
