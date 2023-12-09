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


def tryScript():
    j = 0
    i = 1
    for elm in TIME:
        distance = clacDistance(elm)
        records = checkRecord(DISTANCE[j], distance)
        j+=1
        i *= calcErrorMargin(records)


    return i

result = tryScript()
print(result)

# SECOND PART 

TIME = 44826981
DISTANCE = 202107611381458

def tryScript2():

    distance = clacDistance(TIME)
    records = checkRecord(DISTANCE, distance)


    return distance

result = tryScript2()
print(len(result))