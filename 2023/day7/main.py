from collections import Counter

def get_data():
    fin = open('data.txt', 'r')
    data = [line.strip().split(' ') for line in fin]
    fin.close()
    return data

cards = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J','Q', 'K', 'A']
cards_p2 = ['J', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'Q', 'K', 'A']

def is_five_of_kind(hand):
    return hand.count(hand[0]) == 5

def is_four_of_kind(hand):
    return hand.count(hand[0]) == 4 or hand.count(hand[1]) == 4

def is_full_house(hand):
    if hand.count(hand[0]) == 3:
        return hand.count(hand[1]) == 2 or hand.count(hand[2]) == 2 or hand.count(hand[3]) == 2
    if hand.count(hand[1]) == 3:
        return hand.count(hand[0]) == 2
    return hand.count(hand[2]) == 3 and hand.count(hand[0]) == 2

def is_three_of_kind(hand):
    return hand.count(hand[0]) == 3 or hand.count(hand[1]) == 3 or hand.count(hand[2]) == 3

def is_two_pair(hand):
    unique_pairs_found = 0
    unique_pair_cards = ''
    for card in hand:
        if hand.count(card) == 2 and card not in unique_pair_cards:
            unique_pairs_found += 1
            unique_pair_cards += card
    
    return unique_pairs_found == 2

def is_one_pair(hand):
    for card in hand:
        if hand.count(card) == 2:
            return True
    return False

def is_type_p2(hand, match_func):
    if 'J' not in hand:
        return match_func(hand)
    if hand.count('J') == 5: # edge case
        return True
    # J is best utilized matching the most common card
    other_cards = [card for card in hand if card != 'J']
    most_common = Counter(other_cards).most_common(1)[0][0]

    j_indexes = [i for i, x in enumerate(hand) if x == 'J']
    for j in j_indexes:
        hand[j] = most_common
    return match_func(hand)

def sort_players(players: []):
	for i in range(len(players)):
		for j in range(len(players)-1):
			if need_to_swap(players[j][0], players[j+1][0]):
				players[j], players[j+1] = players[j+1], players[j]
	return players

def sort_players_p2(players: []):
	for i in range(len(players)):
		for j in range(len(players)-1):
			if need_to_swap_p2(players[j][0], players[j+1][0]):
				players[j], players[j+1] = players[j+1], players[j]
	return players


def need_to_swap(hand1, hand2):
    if cards.index(hand1[0]) > cards.index(hand2[0]):
        return True
    if cards.index(hand1[0]) == cards.index(hand2[0]):
        if cards.index(hand1[1]) > cards.index(hand2[1]):
            return True
        if cards.index(hand1[1]) == cards.index(hand2[1]):
            if cards.index(hand1[2]) > cards.index(hand2[2]):
                return True
            if cards.index(hand1[2]) == cards.index(hand2[2]):
                if cards.index(hand1[3]) > cards.index(hand2[3]):
                    return True
                if cards.index(hand1[3]) == cards.index(hand2[3]):
                    if cards.index(hand1[4]) > cards.index(hand2[4]):
                        return True
    return False

def need_to_swap_p2(hand1, hand2):
    if cards_p2.index(hand1[0]) > cards_p2.index(hand2[0]):
        return True
    if cards_p2.index(hand1[0]) == cards_p2.index(hand2[0]):
        if cards_p2.index(hand1[1]) > cards_p2.index(hand2[1]):
            return True
        if cards_p2.index(hand1[1]) == cards_p2.index(hand2[1]):
            if cards_p2.index(hand1[2]) > cards_p2.index(hand2[2]):
                return True
            if cards_p2.index(hand1[2]) == cards_p2.index(hand2[2]):
                if cards_p2.index(hand1[3]) > cards_p2.index(hand2[3]):
                    return True
                if cards_p2.index(hand1[3]) == cards_p2.index(hand2[3]):
                    if cards_p2.index(hand1[4]) > cards_p2.index(hand2[4]):
                        return True
    return False


def main():
    data = get_data()
    hand_types = [[],[],[],[],[],[],[]]
    # put players in their place
    for player in data:
        if is_five_of_kind(player[0]):
            hand_types[6].append(player)
        elif is_four_of_kind(player[0]):
            hand_types[5].append(player)
        elif is_full_house(player[0]):
            hand_types[4].append(player)
        elif is_three_of_kind(player[0]):
            hand_types[3].append(player)
        elif is_two_pair(player[0]):
            hand_types[2].append(player)
        elif is_one_pair(player[0]):
            hand_types[1].append(player)
        else:
            hand_types[0].append(player)
    # rank each hand in each type, better cards are at the front of the map
    for i in range(len(hand_types)):
        hand_types[i] = sort_players(hand_types[i])

    winnings = 0
    players = []
    for hand_type in hand_types:
        players.extend(hand_type)
    
    for rank, player in enumerate(players):
        winnings += (rank + 1) * int(player[1])
    print("part1: ", winnings)

    # part 2
    hand_types = [[],[],[],[],[],[],[]]
    for player in data:
        if is_type_p2(list(player[0]), is_five_of_kind):
            hand_types[6].append(player)
        elif is_type_p2(list(player[0]), is_four_of_kind):
            hand_types[5].append(player)
        elif is_type_p2(list(player[0]), is_full_house):
            hand_types[4].append(player)
        elif is_type_p2(list(player[0]), is_three_of_kind):
            hand_types[3].append(player)
        elif is_type_p2(list(player[0]), is_two_pair):
            hand_types[2].append(player)
        elif is_type_p2(list(player[0]), is_one_pair):
            hand_types[1].append(player)
        else:
            hand_types[0].append(player)
    
    for i in range(len(hand_types)):
        hand_types[i] = sort_players_p2(hand_types[i])

    winnings = 0
    players = []
    for hand_type in hand_types:
        players.extend(hand_type)
    
    for rank, player in enumerate(players):
        winnings += (rank + 1) * int(player[1])
    print("part2: ", winnings)
    

    



if __name__ == '__main__':
    main()