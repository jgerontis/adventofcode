
def main():
    fin = open('test_data.txt', 'r')
    line = fin.readline()
    seeds = line[7:].strip().split(' ')
    line = fin.readline() # dummy line
    line = fin.readline() # dummy line
    seed_to_soil_map = []
    reading = True
    while reading:
        line = fin.readline()
        if line == '\n':
            reading = False
        else:
            seed_to_soil_map.append(line.strip().split(' '))
    
    print('soil')
    line = fin.readline() # dummy line
    

    soil_to_fertilizer_map = []
    reading = True
    while reading:
        line = fin.readline()
        

        if line == '\n':
            reading = False
        else:
            soil_to_fertilizer_map.append(line.strip().split(' '))
    print('fertilizer')

    line = fin.readline() # dummy line
    

    fertilizer_to_water_map = []
    reading = True
    while reading:
        line = fin.readline()
        

        if line == '\n':
            reading = False
        else:
            fertilizer_to_water_map.append(line.strip().split(' '))

    print('water')
    line = fin.readline() # dummy line
    

    water_to_light_map = []
    reading = True
    while reading:
        line = fin.readline()
        

        if line == '\n':
            reading = False
        else:
            water_to_light_map.append(line.strip().split(' '))
    
    print('light')
    line = fin.readline() # dummy line
    

    light_to_temperature_map = []
    reading = True
    while reading:
        line = fin.readline()
        

        if line == '\n':
            reading = False
        else:
            light_to_temperature_map.append(line.strip().split(' '))
    
    print('temperature')
    line = fin.readline() # dummy line
    

    temperature_to_humidity_map = []
    reading = True
    while reading:
        line = fin.readline()
        

        if line == '\n':
            reading = False
        else:
            temperature_to_humidity_map.append(line.strip().split(' '))

    print('humidity')
    line = fin.readline() # dummy line
    

    humidity_to_location_map = []
    reading = True
    while reading:
        line = fin.readline()
        if line == '\n' or line == '':
            reading = False
        else:
            humidity_to_location_map.append(line.strip().split(' '))
    

    locations = []
    for seed in seeds:
        seed = int(seed)
        print('working on seed:', seed)
        soil = get_destination_value(seed_to_soil_map, seed)
        fertilizer = get_destination_value(soil_to_fertilizer_map, soil)
        water = get_destination_value(fertilizer_to_water_map, fertilizer)
        light = get_destination_value(water_to_light_map, water)
        temperature = get_destination_value(light_to_temperature_map, light)
        humidity = get_destination_value(temperature_to_humidity_map, temperature)
        locations.append(get_destination_value(humidity_to_location_map, humidity))

    print(min(locations))


def get_destination_value(map, input):
    for row in map:
        if input >= int(row[1]) and input < int(row[1])+int(row[2]):
            position = input - int(row[1])
            return int(row[0]) + position
    return input

    
if __name__ == '__main__':
    main()
