def get_data():
    data = []
    fin = open('data.txt', 'r')
    for line in fin:
        data.append(line.strip())
    fin.close()
    return data

def parse_line(line):
    left, right = line.split('|')
    left = left[10:].split()
    right = right.split()
    return left, right

def score_per_card(left, right):
    matches = 0
    for num in right:
        if num in left:
            matches += 1
    return matches

def main():
    data = get_data()
    total = 0
    lefts = []
    rights = []
    for line in data:
        left, right = parse_line(line)
        lefts.append(left)
        rights.append(right)
    # part1
    for i in range(len(lefts)):
        matches = score_per_card(lefts[i], rights[i])
        if matches > 0:
            total += 2 ** (matches - 1)
    print("part1: ", total)
    # part2
    copies = [1] * len(lefts)
    for i in range(len(lefts)):
        matches = score_per_card(lefts[i], rights[i])
        j = i+1
        while matches > 0:
            if j < len(lefts):
                copies[j] += copies[i]
                matches -= 1
                j += 1
            else:
                break

    print("part2: ", sum(copies))

if __name__ == '__main__':
    main()
