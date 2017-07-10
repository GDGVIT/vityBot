import string_functions
import handle_query


inp = str()

while inp != 'q':
    inp = raw_input('>>')

    faculty = string_functions.find_match(inp)

    if faculty is None:
        print "can't get you"
        continue

    keywords = string_functions.get_keyword(inp)
    response = handle_query.get_response(keywords, faculty)

    print response