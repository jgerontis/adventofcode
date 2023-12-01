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


def value(line: str) -> int:
    value = ''
    # forward
    for i in range(len(line)):
        if line[i].isdigit():
            value += line[i]
            break
        num = wordsToNums(line[i:])
        if num:
            value += num
            break
    num = None
    #backward
    for i in reversed(range(len(line))):
        if line[i].isdigit():
            value += line[i]
            break
        num = wordsToNums(line[i:])
        if num:
            value += num
            break
    return int(value)

def main():
    fin = open('data.txt', 'r')
    total = 0
    for line in fin:
        line = line.strip()
        total += value(line)
    print(total)

if __name__ == '__main__':
    main()