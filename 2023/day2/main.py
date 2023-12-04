def get_data():
    data = []
    fin = open('data.txt', 'r')
    for line in fin:
        line = line.strip().split(':')
        data.append(line)
    fin.close()
    return data

def legal_game(game: str) -> bool:
    colors = game.split(',')
    for color in colors:
        if 'green' in color:
            temp = int(color[:-6])
            if temp > 13:
                return False
        if 'red' in color:
            temp = int(color[:-4])
            if temp > 12:
                return False
        if 'blue' in color:
            temp = int(color[:-5])
            if temp > 14:
                return False
    return True

def min_cubes_power_sum(games: list) -> int:
    max_red = 0
    max_green = 0
    max_blue = 0
    reds = []
    greens = []
    blues = []
    for game in games:
        colors = game.split(',')
        for color in colors:   
            if 'red' in color:
                reds.append(int(color[:-4]))
            if 'green' in color:
                greens.append(int(color[:-6]))
            if 'blue' in color:
                blues.append(int(color[:-5]))
    max_red = max(reds)
    max_green = max(greens)
    max_blue = max(blues)
    return max_red * max_green * max_blue


def main():
    data = get_data()
    total = 0
    for line in data:
        id = int(line[0][5:])
        games = line[1].split(';')
        valid = True
        for game in games:
            if not legal_game(game):
                valid = False
        if valid:
            total += id
    print("part1: ", total)

    total = 0
    for line in data:
        games = line[1].split(';')
        power_sum = min_cubes_power_sum(games)
        total += power_sum
    print("part2: ", total)

if __name__ == '__main__':
    main()