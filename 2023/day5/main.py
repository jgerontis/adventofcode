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

# given a seed range, returns a list of mapped seed ranges
# can return more than 1 if the seed range is split
# (it didn't perfectly fit)
def get_mapped_pairs(seed_range: list, m: list):
    result = []
    seed_start = seed_range[0]
    seed_span = seed_range[1]
    # we sort the maps so that if a seed range is too large,
    # we can immediately try it again on the next biggest map
    # without worrying about if we missed it
    for dest, src, span in sorted(m, key=lambda x:x[1]):
        position = seed_start - src
        # if the seed start is within the src range
        if seed_start >= src and seed_start < src + span:
            # map the new start relative to the dest
            new_start = dest + position
            # if the seed range is completely contained in the map range
            if src + span >= seed_start + seed_span:
                result.append([new_start, seed_span])
            else:
                # since it didn't fit, we see how much didn't fit
                remaining_span = (seed_start + seed_span) - (src + span)
                # we add the part that did fit to the result
                result.append((new_start, seed_span - remaining_span))
                # re-use the original variables with the remaining span
                seed_span = remaining_span
                seed_start = src + span
    if not result:
        result.append(seed_range)
    return result


def main():
    seeds, maps = get_data()
    # seeds is a list
    # maps is 3 deep, i.e map[soil:[[dest,src,range],...], fertilizer:[[dest,src,range],...],...]
    for i in range(len(seeds)):
        for m in maps:
            seeds[i] = get_next_value(seeds[i], m)
    print("part1: ", min(seeds))

    # part2
    # since there's millions of inputs, we just treat them as ranges
    # we need to see each seed range all the way through to the end before 
    # moving on to the next pair since the ranges can be split for more results
    seeds, maps = get_data()
    result = []
    seed_pairs = list(zip(seeds[::2], seeds[1::2]))
    seed_ranges = [range(start, end+1) for start, end in zip(seeds[::2], seeds[1::2])]

    for sp in seed_pairs:
        seed_ranges = [sp]
        for m in maps:
            new_s = []
            for s in seed_ranges:
                new_s.extend(get_mapped_pairs(s, m))
            seed_ranges = new_s[:]
        result.append(min(x for x, _ in seed_ranges))
    print(min(result))

if __name__ == '__main__':
    main()