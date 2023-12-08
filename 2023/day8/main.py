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
    print(step)
            

        


if __name__ == '__main__':
    main()