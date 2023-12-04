from main import near_symbol, get_number

def test_part1():
    data = [
        "467..114..",
        "...*......",
        "..35..633.",
        "......#...",
        "617*......",
        ".....+.58.",
        "..592.....",
        "......755.",
        "...$.*....",
        ".664.598.."
    ]
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
    test_part1()
    # test_get_number()