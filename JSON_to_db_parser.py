import json
import os
import psycopg2

listOfDicts = []

directoryList = os.listdir("./output")

for file in directoryList:
    with open("./output/"+file) as json_data:
        loader = json.load(json_data)
    listOfDicts.append(loader)

conn = psycopg2.connect(database='vityBot', user='initiator26', host='localhost', port=8000)
conn.set_session(autocommit=True)

cur = conn.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS faculty (empid INT PRIMARY KEY, division STRING, school STRING, name STRING,
            designation STRING, open_hours STRING, intercom INT, email STRING, room STRING)""")

for di in listOfDicts:
    keys = tuple(di.keys())
    values = tuple(di.values())
    conn.execute('INSERT INTO faculty '+str(keys)+' VALUES '+str(values))

cur.close()
conn.close()
