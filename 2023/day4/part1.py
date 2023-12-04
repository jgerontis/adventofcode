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
    if matches == 0:
        return 0
    return 2 ** (matches - 1)

def main():
    fin = open('data.txt', 'r')
    total = 0
    lefts = []
    rights = []
    for line in fin:
        left, right = parse_line(line)
        lefts.append(left)
        rights.append(right)
    for i in range(len(lefts)):
        total += score_per_card(lefts[i], rights[i])
    print(total)

main()