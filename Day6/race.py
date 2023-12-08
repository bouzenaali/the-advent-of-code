TIME = [44, 82, 69, 81]
DISTANCE = [202, 1076, 1138, 1458]

def clacDistance(time):
    distance = []
    for sec in range(time):
        raceTime = (time - sec)
        speed = sec
        distance.append(speed*raceTime)
    return distance


def checkRecord(record, distance):
    bestRecord = []
    for dist in distance:
        if dist > record:
            bestRecord.append(dist)
    return bestRecord


def calcErrorMargin(records):
    i = len(records)
    return i


def tryScript(time, distance):
    j = 0
    i = 1
    for elm in TIME:
        distance = clacDistance(elm)
        records = checkRecord(DISTANCE[j], distance)
        j+=1
        i *= calcErrorMargin(records)


    return i

result = tryScript(TIME, DISTANCE)
print(result)