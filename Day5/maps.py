seedToSoil = []
soilToFertilizer = []
fertilizerToWater = []
waterToLight = []
lightToTemperature = []
temperatureToHumidity = []
humidityToLocation = []

def createMaps():
    seed_to_soil = False   
    soil_to_fertilizer = False
    fertilizer_to_water = False
    water_to_light = False
    light_to_temperature = False
    temperature_to_humidity = False
    humidity_to_location = False

    with open("Day5/test.txt", "r") as file:
        for line in file:
            line = line.strip()

            if line.startswith("seed-to-soil map:"):
                seed_to_soil = True   
                soil_to_fertilizer = False
                fertilizer_to_water = False
                water_to_light = False
                light_to_temperature = False
                temperature_to_humidity = False
                humidity_to_location = False
            elif seed_to_soil and line:
                try:
                    dist, src, length = map(int,line.split())
                    seedToSoil.append((dist, src, length))
                except ValueError:
                    print(f"Skipping line: {line}")

            elif line.startswith("soil-to-fertilizer map:"):
                soil_to_fertilizer = True
                seed_to_soil = False  
                fertilizer_to_water = False
                water_to_light = False
                light_to_temperature = False
                temperature_to_humidity = False
                humidity_to_location = False
            elif soil_to_fertilizer and line:
                try:
                    dist, src, length = map(int,line.split())
                    soilToFertilizer.append((dist, src, length))
                except ValueError:
                    print(f"Skipping line: {line}")

            elif line.startswith("fertilizer-to-water map:"):
                fertilizer_to_water = True
                seed_to_soil = False
                soil_to_fertilizer = False
                water_to_light = False
                light_to_temperature = False
                temperature_to_humidity = False
                humidity_to_location = False
            elif fertilizer_to_water and line:
                try:
                    dist, src, length = map(int,line.split())
                    fertilizerToWater.append((dist, src, length))
                except ValueError:
                    print(f"Skipping line: {line}")

            elif line.startswith("water-to-light map:"):
                seed_to_soil = False
                soil_to_fertilizer = False
                fertilizer_to_water = False
                water_to_light = True
                light_to_temperature = False
                temperature_to_humidity = False
                humidity_to_location = False
            elif water_to_light and line:
                try:
                    dist, src, length = map(int,line.split())
                    waterToLight.append((dist, src, length))
                except ValueError:
                    print(f"Skipping line: {line}")

            elif line.startswith("light-to-temperature map:"):
                seed_to_soil = False
                soil_to_fertilizer = False
                fertilizer_to_water = False
                water_to_light = False
                light_to_temperature = True
                temperature_to_humidity = False
                humidity_to_location = False
            elif light_to_temperature and line:
                try:
                    dist, src, length = map(int,line.split())
                    lightToTemperature.append((dist, src, length))
                except ValueError:
                    print(f"Skipping line: {line}")

            elif line.startswith("temperature-to-humidity map:"):
                seed_to_soil = False
                soil_to_fertilizer = False
                fertilizer_to_water = False
                water_to_light = False
                light_to_temperature = False
                temperature_to_humidity = True
                humidity_to_location = False
            elif temperature_to_humidity and line:
                try:
                    dist, src, length = map(int,line.split())
                    temperatureToHumidity.append((dist, src, length))
                except ValueError:
                    print(f"Skipping line: {line}")

            elif line.startswith("humidity-to-location map:"):
                seed_to_soil = False
                soil_to_fertilizer = False
                fertilizer_to_water = False
                water_to_light = False
                light_to_temperature = False
                temperature_to_humidity = False
                humidity_to_location = True
            elif humidity_to_location and line:
                try:
                    dist, src, length = map(int,line.split())
                    humidityToLocation.append((dist, src, length))   
                except ValueError:
                    print(f"Skipping line: {line}")
    return seedToSoil, soilToFertilizer, fertilizerToWater, waterToLight, lightToTemperature, temperatureToHumidity, humidityToLocation