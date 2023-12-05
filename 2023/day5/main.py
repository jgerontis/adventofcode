def get_data():
    with open('data.txt') as fin:
        lines = [l.strip() for l in fin.readlines()]
    
    # parse the seeds
    line = lines.pop(0) # dummy line
    parts = line.split(': ')
    numbers_string = parts[1]
    numbers = numbers_string.split()
    seeds = [int(s) for s in numbers]
    lines.pop(0) # dummy line

    # parse the maps
    maps = []
    while lines:
        line = lines.pop(0)
        if line.endswith('map:'):
            current = []
            continue
        if line == '':
            maps.append(current)
            continue
        current.append([int(n) for n in line.split()])
    maps.append(current)
    return seeds, maps

# given a seed, returns the mapped value
def get_next_value(seed, m):
    for dest, src, span in m:
        if seed >= src and seed < src + span:
            position = seed - src
            return dest + position
    return seed


def main():
    seeds, maps = get_data()
    # seeds is a list
    # maps is 3 deep, i.e map[soil:[[dest,src,range],...], fertilizer:[[dest,src,range],...],...]

    for i in range(len(seeds)):
        for m in maps:
            seeds[i] = get_next_value(seeds[i], m)
    print(min(seeds))

if __name__ == '__main__':
    main()