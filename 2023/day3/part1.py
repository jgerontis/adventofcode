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
                current_number += char
            else:
                if current_number != '' and part_number:
                    total += int(current_number)
                current_number = ''
                part_number = False
    print(total)



if __name__ == '__main__':
    main()  