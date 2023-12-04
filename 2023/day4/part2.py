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
    fin = open('data.txt', 'r')
    total = 0
    lefts = []
    rights = []
    copies = []
    for line in fin:
        left, right = parse_line(line)
        lefts.append(left)
        rights.append(right)
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

    print(sum(copies))

main()