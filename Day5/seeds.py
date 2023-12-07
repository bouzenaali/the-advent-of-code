# MAPS
from maps import createMaps
seeds, seedToSoil, soilToFertilizer, fertilizerToWater, waterToLight, lightToTemperature, temperatureToHumidity, humidityToLocation = createMaps()


# CONVERTERS
def seedToSoilConv(Map, conv):
    soils = []
    for element in conv:
        transformed = False
        for dest, src, length in Map:
            if element >= src and element < (src + length):
                soils.append(dest + (element - src))
                transformed = True
                break
        
        if not transformed:
            soils.append(element)

    return soils
    

def soilToFertilizerConv(Map, conv):
    fertilizers = []

    for element in conv:
        transformed = False
        for dest, src, length in Map:
            if element >= src and element < (src + length):
                fertilizers.append(dest + (element - src))
                transformed = True
                break

        if not transformed:
            fertilizers.append(element)

    return fertilizers


def fertilizerToWaterConv(Map, conv):
    waters = []

    for element in conv:
        transformed = False
        for dest, src, length in Map:
            if element >= src and element < (src + length):
                waters.append(dest + (element - src))
                transformed = True
                break

        
        if not transformed:
            waters.append(element)

    return waters


def waterToLightConv(Map, conv):
    lights = []
        
    for element in conv:
        transformed = False
        for dest, src, length in Map:
            if element >= src and element < (src + length):
                lights.append(dest + (element - src))
                transformed = True
    
        if not transformed:
            lights.append(element)

    return lights


def lightToTemperatureConv(Map, conv):
    temperatures = []

    for element in conv:
        transformed = False
        for dest, src, length in Map:
            if element >= src and element < (src + length):
                temperatures.append(dest + (element - src))
                transformed = True
                break

        if not transformed:
            temperatures.append(element)

    return temperatures


def temperatureToHumidityConv(Map, conv):
    humidities = []

    for element in conv:
        transformed = False
        for dest, src, length in Map:
            if element >= src and element < (src + length):
                humidities.append(dest + (element - src))
                transformed = True

    
        if not transformed:
                humidities.append(element)

    return humidities


def humidityToLocationConv(Map, conv):
    locations = []

    for element in conv:
        transformed = False
        for dest, src, length in Map:
            if element >= src and element < (src + length):
                locations.append(dest + (element - src))
                transformed = True

    
        if not transformed:
                locations.append(element)

    return locations



# TEST
def tryConverters():
    soils = seedToSoilConv(seedToSoil, seeds)
    fertilizers = soilToFertilizerConv(soilToFertilizer, soils)
    waters = fertilizerToWaterConv(fertilizerToWater, fertilizers)
    lights = waterToLightConv(waterToLight, waters)
    temperatures = lightToTemperatureConv(lightToTemperature, lights)
    humidities = temperatureToHumidityConv(temperatureToHumidity, temperatures)
    locations = humidityToLocationConv(humidityToLocation, humidities)

    lowest_loc = min(locations)
    print(f"the lowest location is: {lowest_loc}")
    

tryConverters()