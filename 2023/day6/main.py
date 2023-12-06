def main():
    fin = open('data.txt', 'r')
    times = fin.readline().strip().split(':')[1].split()
    distances = fin.readline().strip().split(':')[1].split()

    total = 1
    for i in range(len(times)):
        time = times[i]
        distance = distances[i]
        total *= calculate_options(int(time), int(distance))
    print("part1: ", total)

    time = int(''.join(map(str,times)))
    distance = int(''.join(map(str,distances)))
    print("part2: ", calculate_options(time, distance))

def calculate_options(time, record):
    options_count = 0
    for i in range(1, time):
        if (time - i) * i > record:
            options_count += 1
    return options_count

if __name__ == '__main__':
    main()