import math

def getPercent(a, b):
    return int(math.ceil(float(a) / float(b) * 100.00))

def getAverage(li):
    count = 0
    sum = 0

    for i in li:
        sum += i
        count += 1

    return sum / count
