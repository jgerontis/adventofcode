def get_data():
    with open('data.txt', 'r') as f:
        return f.read().splitlines()

def wordsToNums(line: str) -> str:
    numbers = {
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9',
        'ten': '10'
    }
    for word, num in numbers.items():
        if line.startswith(word):
            return num


def value(line: str, part2=False) -> int:
    value = ''
    # forward
    for i in range(len(line)):
        if line[i].isdigit():
            value += line[i]
            break
        num = wordsToNums(line[i:])
        if num and part2:
            value += num
            break
    num = None
    #backward
    for i in reversed(range(len(line))):
        if line[i].isdigit():
            value += line[i]
            break
        num = wordsToNums(line[i:])
        if num and part2:
            value += num
            break
    return int(value)

def main():
    data = get_data()
    total = 0
    for line in data:
        total += value(line)
    print("part1: ", total)

    total = 0
    for line in data:
        total += value(line, True)
    print("part2: ", total)

if __name__ == '__main__':
    main()