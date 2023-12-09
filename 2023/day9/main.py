def get_data():
    fin = open('data.txt', 'r')
    data = []
    for line in fin:
        line = list(line.strip().split(' '))
        data.append(list(map(int, line)))
    fin.close()
    return data

def get_value(row: list):
    triangle = [row]
    level = 0
    while True:
        triangle.append([])
        for i in range(len(triangle[level])-1):
            diff = triangle[level][i+1] - triangle[level][i]
            triangle[level+1].append(diff)
        if diff == 0 or len(triangle[level+1]) == 0:
            break
        level += 1
    level = len(triangle) - 1
    triangle[-1].append(0)
    while level > 0:   
        triangle[level-1].append(triangle[level-1][-1] + triangle[level][-1])
        level -= 1
    return triangle[0][-1]

# tried reversing the input but it didn't work, so here I am doing it manually :(
def get_value_p2(row: list):
    triangle = [row]
    level = 0
    while True:
        triangle.append([])
        for i in range(len(triangle[level])-1):
            diff = triangle[level][i+1] - triangle[level][i]
            triangle[level+1].append(diff)
        if diff == 0 or len(triangle[level+1]) == 0:
            break
        level += 1
    level = len(triangle) - 1
    triangle[-1].insert(0, 0)
    while level > 0:   
        triangle[level-1].insert(0, (triangle[level-1][0] - triangle[level][0]))
        level -= 1
    return triangle[0][0]

def main():
    data = get_data()
    p1_total = 0
    p2_total = 0
    for row in data:
        p1_total += get_value(row.copy())
        p2_total += get_value_p2(row) # still mad reversing the input didn't work with my algorithm
    print("part1: ", p1_total)
    print("part2: ", p2_total)    

if __name__ == '__main__':
    main()
    