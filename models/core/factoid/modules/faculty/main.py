# scripts to test the interfaces

import string_functions
import handle_query


inp = str()

while True:
    inp = raw_input('>>')
    if inp == 'q':
        break

    response = handle_query.process_query(inp)
    print response