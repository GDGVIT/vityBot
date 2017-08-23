def get_keyword(query):
    if 'classes' in query:
        if 'today' in query:
            return ['classes', 'today']
        if 'end' in query:
            return ['classes', 'end']
    elif 'class' in query:
        if 'now' in query or 'current' in query:
            return ['class', 'current']
        elif 'next' in query:
            return ['class', 'next']
