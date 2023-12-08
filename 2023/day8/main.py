import math

def get_data():
    fin = open('data.txt', 'r')
    steps = fin.readline().strip()
    fin.readline() # dummy line
    mappings = {}
    for line in fin:
        line = line.strip()
        mappings[line[0:3]] = [line[7:10], line[12:15]]
    fin.close()
    return steps, mappings

def LR(step: str):
    if step == 'L':
        return 0
    return 1

def main():
    steps, maps = get_data()
    step = 0
    target = 'AAA'
    while target != 'ZZZ':
        i = LR(steps[step%len(steps)])
        target = maps[target][i]
        step += 1
    print("part1: ", step)

    start_keys = []
    for key in maps.keys():
        if key.endswith('A'):
            start_keys.append(key)
    print(start_keys)

    step_list = [0] * len(start_keys)
    for i, key in enumerate(start_keys):
        while not key.endswith('Z'):
            key = maps[key][LR(steps[step_list[i]%len(steps)])]
            step_list[i] += 1
    print(step_list)
    print("part 2: ", math.lcm(*step_list))
            

        


if __name__ == '__main__':
    main()