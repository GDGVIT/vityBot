import psycopg2

con = psycopg2.connect(dbname = 'vit', user = 'surya2', host = 'localhost', port = 26257)
con.set_session(autocommit = True)

cur = con.cursor()

def getRow(query):
    global cur
    global con

    cur.execute(query)

    row = cur.fetchall()

    return row[0]

    cur.close()
    con.close()
