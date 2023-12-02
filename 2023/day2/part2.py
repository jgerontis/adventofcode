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
    fin = open('data.txt', 'r')
    total = 0
    for line in fin:
        line = line.strip().split(':')
        games = line[1].split(';')
        power_sum = min_cubes_power_sum(games)
        total += power_sum
    print(total)

if __name__ == '__main__':
    main()