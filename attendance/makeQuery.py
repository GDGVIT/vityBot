import extractor
import dbmath
import database as db

query = 'SELECT '

subs = ['DLM', 'DSA', 'PHY', 'MAT']


def isDebarred(percent):
    return True if percent < 75 else False


def setID(id):
    """
    appends the id for the condition in a query
    """
    global query

    query += 'WHERE regid = ' + id + ';'


def makeQuery(id, keywords):
    """
    function appends the query with columns required
    also displays corresponding output from db based on the query
    """
    global query
    global subs

    subsInQuery = extractor.intersection_list(keywords, subs)

    if 'attendance' in keywords and subsInQuery == '':
        query += 'DLM_AC, DLM_TC, DSA_AC, DSA_TC, PHY_AC, PHY_TC, MAT_AC, MAT_TC FROM attendance '
        setID(id)

        row = db.getRow(query)

        # print row

        percents = list()  # contain attendance percentage in each subject
        percents.append(dbmath.getPercent(row[0], row[1]))
        percents.append(dbmath.getPercent(row[2], row[3]))
        percents.append(dbmath.getPercent(row[4], row[5]))
        percents.append(dbmath.getPercent(row[6], row[7]))

        count = 0
        for i in percents:
            print subs[count], ' : ',
            print i, ' ',
            count += 1

        print '\nyour attendance average is ', dbmath.getAverage(percents)


    elif 'attendance' in keywords and subsInQuery != '':
        query += subsInQuery + '_AC, ' + subsInQuery + '_TC ' + 'FROM attendance '

        setID(id)

        row = db.getRow(query)

        percent = dbmath.getPercent(row[0], row[1])

        print 'your average in ', subsInQuery, ' is ', percent


    elif 'debarred' in keywords and subsInQuery == '':  # print subjects debarred
        query += 'DLM_AC, DLM_TC, DSA_AC, DSA_TC, PHY_AC, PHY_TC, MAT_AC, MAT_TC' \
                 ' FROM attendance '
        setID(id)

        row = db.getRow(query)

        percents = list()
        percents.append(dbmath.getPercent(row[0], row[1]))
        percents.append(dbmath.getPercent(row[2], row[3]))
        percents.append(dbmath.getPercent(row[4], row[5]))
        percents.append(dbmath.getPercent(row[6], row[7]))

        count = 0
        flag = True
        while count < 4:
            if isDebarred(percents[count]):
                print 'you are debarred in ', subs[count], ' (', percents[count], ')'
                flag = False

            if count == 3 and flag:
                print 'you are not debarred in any subs'

            count += 1

    elif 'debarred' in keywords and subsInQuery != '':
        query += subsInQuery + '_AC, ' + subsInQuery + '_TC ' + 'FROM attendance '
        setID(id)

        row = db.getRow(query)

        percent = dbmath.getPercent(row[0], row[1])

        if isDebarred(percent):
            print 'you are debarred in ', subsInQuery, ' (', percent, ')'
        else:
            print 'you are not debarred in ', percent
