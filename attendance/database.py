import psycopg2

con = psycopg2.connect(dbname='vit', user='surya2',
                       host='localhost', port=26257)

con.set_session(autocommit=True)

cur = con.cursor()


def getRow(query):
    """
    The function takes in an SQL query and
    gathers all rows in table that match the condition.
    cursor fetches rows into a list(the table) of tuples(rows)

    function returns the first tuple in the list - there is only 1 row for an ID
    """
    global cur
    global con

    cur.execute(query)

    row = cur.fetchall()

    cur.close()  # close the cursor
    con.close()  # close the connection to database

    return row[0]
