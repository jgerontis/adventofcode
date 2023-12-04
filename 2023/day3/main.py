def get_data():
    data = []
    fin = open('data.txt', 'r')
    for line in fin:
        line=line.strip()
        data.append(line)
    fin.close()
    return data

def is_symbol(char) -> bool:
    return not char.isdigit() and char != '.'

# seeks to the start of a number and returns it
def get_number(data, row, col) -> str:
    char = data[row][col]
    if not char.isdigit():
        return ''
    num = ''
    # seek to start of number
    while col > 0 and data[row][col-1].isdigit():
        col -= 1
    # build the number from start to end
    while col < len(data[row]) and data[row][col].isdigit():
        num += data[row][col]
        col += 1
    return num
    
# returns true if there is a symbol near the given row and col
def near_symbol(data, row, col, row_length) -> bool:
    if row > 0:
        # check above
        if is_symbol(data[row - 1][col]):
            return True
        # check top left
        if col > 0 and is_symbol(data[row - 1][col - 1]):
            return True
        # check top right
        if col < row_length - 1 and is_symbol(data[row - 1][col + 1]):
            return True
    if row < len(data) - 1:
        # check below
        if is_symbol(data[row + 1][col]):
            return True
        # check bottom left
        if col > 0 and is_symbol(data[row + 1][col - 1]):
            return True
        # check bottom right
        if col < row_length - 1 and is_symbol(data[row + 1][col + 1]):
            return True
    if col > 0:
        # check left
        if is_symbol(data[row][col - 1]):
            return True
    if col < row_length - 1:
        # check right
        if is_symbol(data[row][col + 1]):
            return True
    return False

# returns gear product if valid gear, else 0
def is_gear(data, row, col, row_length) -> int:
    if data[row][col] != '*':
        return 0
    neighbors = []
    if row > 0:
        # check above
        above = get_number(data, row - 1,col)
        if above != '':
            neighbors.append(above)
        else:
            # check top left
            if col > 0:
                top_left = get_number(data, row - 1, col - 1)
                if top_left != '':
                    neighbors.append(top_left)
            # check top right
            if col < row_length - 1:
                top_right = get_number(data, row - 1, col + 1)
                if top_right != '':
                    neighbors.append(top_right)
    # check below
    if row < len(data) - 1:
        below = get_number(data, row + 1, col)
        if below != '':
            neighbors.append(below)
        else:
            # check bottom left
            if col > 0:
                bottom_left = get_number(data, row + 1, col - 1)
                if bottom_left != '':
                    neighbors.append(bottom_left)
            # check bottom right
            if col < row_length - 1:
                bottom_right = get_number(data, row + 1, col + 1)
                if bottom_right != '':
                    neighbors.append(bottom_right)
    # check left
    if col > 0:
        left = get_number(data, row, col - 1)
        if left != '':
            neighbors.append(left)
    # check right
    if col < row_length - 1:
        right = get_number(data, row, col + 1)
        if right != '':
            neighbors.append(right)
    if len(neighbors) == 2:
        return int(neighbors[0]) * int(neighbors[1])
    return 0

def main():
    data = get_data()
    total = 0
    # We're going to read one char at a time.
    # As we find numbers, we'll search around them for symbols
    # If we find a symbol, we'll be sure to mark this as a part_number
    # and add it to the running total once we have the whole number
    for row in range(len(data)):
        current_number = ''
        part_number = False
        for col, char in enumerate(data[row]):
            if char.isdigit():
                if near_symbol(data, row, col, len(data[row])):
                    part_number = True
                    current_number = get_number(data, row, col)
            else:
                if current_number != '' and part_number:
                    total += int(current_number)
                current_number = ''
                part_number = False
            if current_number != '' and part_number and col == len(data[row]) - 1:
                total += int(current_number)
    print("part1: ", total)
    # we're going to read a char at a time again,
    # but this time we're going to look for gears
    # and check if it has exactly 2 numbers around it
    total = 0
    for row in range(len(data)):
        for col, char in enumerate(data[row]):
            gear_value = is_gear(data, row, col, len(data[row]))
            if gear_value != 0:
                total += gear_value
    print("part2: ", total)





if __name__ == '__main__':
    main()  