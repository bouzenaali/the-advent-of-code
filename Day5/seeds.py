from maps import createMaps





# CONVERTERS
# def seedToSoil(src, dist):
#     return
# def soilToFertilizer(src, dist):
#     return
# def fertilizerToWater(src, dist):
#     return
# def waterToLight(src, dist):
#     return
# def lightToTemperature(src, dist):
#     return
# def temperatureToHumidity(src, dist):
#     return
# def humidityToLocation(src, dist):
#     return



# TEST

seeds, seedToSoil, soilToFertilizer, fertilizerToWater, waterToLight, lightToTemperature, temperatureToHumidity, humidityToLocation = createMaps()

print(f"seeds: {seeds}")
print(f"seeds to soil map: {seedToSoil}")
print(f"soil to fertilizer: {soilToFertilizer}")
print(f"fertilizer to water: {fertilizerToWater}")
print(f"water to light: {waterToLight}")
print(f"light to temperature: {lightToTemperature}")
print(f"temperature to humidity: {temperatureToHumidity}")
print(f"humidity to location: {humidityToLocation}")