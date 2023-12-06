def seedToSoil(src, dist):
    return
def soilToFertilizer(src, dist):
    return
def fertilizerToWater(src, dist):
    return
def waterToLight(src, dist):
    return
def lightToTemperature(src, dist):
    return
def temperatureToHumidity(src, dist):
    return
def humidityToLocation(src, dist):
    return




def tryConverter():
    with open("Day5/test.txt", "r") as file:
        for line in file:
            if "seeds" in line:
                seeds = line.split()
                seeds = seeds[1:]
            
            

tryConverter()