seeds = []
seedToSoil = []
soilToFertilizer = []
fertilizerToWater = []
waterToLight = []
lightToTemperature = []
temperatureToHumidity = []
humidityToLocation = []

def createMaps():

    current_map = None
    with open("Day5/test.txt", "r") as file:
        for line in file:
            line = line.strip()

            if line.startswith("seeds:"):
                seeds = line.split()
                seeds = seeds[1:]
            elif line.startswith("seed-to-soil map:"):
                current_map = seedToSoil
            elif line.startswith("soil-to-fertilizer map:"):
                current_map = soilToFertilizer
            elif line.startswith("fertilizer-to-water map:"):
                current_map = fertilizerToWater
            elif line.startswith("water-to-light map:"):
                current_map = waterToLight
            elif line.startswith("light-to-temperature map:"):
                current_map = lightToTemperature
            elif line.startswith("temperature-to-humidity map:"):
                current_map = temperatureToHumidity
            elif line.startswith("humidity-to-location map:"):
                current_map = humidityToLocation

            elif current_map is not None and line:
                try:
                    dist, src, length = map(int, line.split())
                    current_map.append((dist, src, length))
                except ValueError:
                    print(f"Skipping line: {line}")

                  

    return seeds, seedToSoil, soilToFertilizer, fertilizerToWater, waterToLight, lightToTemperature, temperatureToHumidity, humidityToLocation