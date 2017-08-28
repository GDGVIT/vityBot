def get_keyword(query):
    if 'classes' in query:
        if 'today' in query:
            return ['classes', 'today']
        elif 'end' in query:
            return ['classes', 'end']
        elif 'tomorrow' in query:
            return ['classes', 'tomorrow']
        else:
            return ['classes', 'today']
    elif 'class' in query:
        if 'now' in query or 'current' in query:
            return ['class', 'current']
        elif 'next' in query:
            return ['class', 'next']
