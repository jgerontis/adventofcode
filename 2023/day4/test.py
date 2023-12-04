from part2 import score_per_card

def test():
    lefts = [
        [41,48,83,86,17],
        [13,32,20,16,61],
        [1,21,53,59,44],
        [41,92,73,84,69],
        [87,83,26,28,32],
        [31,18,13,56,72],
    ]
    rights = [
        [83,86,6,31,17,9,48,53],
        [61,30,68,82,17,32,24,19],
        [69,82,63,72,16,21,14,1],
        [59,84,76,51,58,5,54,83],
        [88,30,70,12,93,22,82,36],
        [74,77,10,23,35,67,36,11]
    ]

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

test()