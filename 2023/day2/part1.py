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


def main():
    fin = open('data.txt', 'r')
    total = 0
    for line in fin:
        line = line.strip().split(':')
        id = int(line[0][5:])
        games = line[1].split(';')
        valid = True
        for game in games:
            if not legal_game(game):
                valid = False
        if valid:
            total += id
    print(total)

if __name__ == '__main__':
    main()