from collections import defaultdict

#create dictoionary in order to rank hands
card_order_dict = {"2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "T": 10, "J": 11, "Q": 12, "K": 13, "A": 14, "0": 0, "1": 1}

#main function to score hand by asigning ranking hands 
#could change x to hand
def score_my_hand(hand):
    # x is a list of seven cards

    # sort out base score
    score = 0
    if check_straight_flush(hand):
        score = 1000
    elif check_four_of_a_kind(hand):
        score = 900
    elif check_full_house(hand):
        score = 800
    elif check_flush(hand):
        score = 700
    elif check_straight(hand):
        score = 600
    elif check_three_of_a_kind(hand):
        score = 500
    elif check_two_pairs(hand):
        score = 400
    elif check_one_pairs(hand):
        score = 300

    # if there is an issue with highest card, the following function differentiates this (split pot conditions)

    High_card = check_high_card(hand)
    score = score + High_card
    return score

# various functions to check for certain hands
def check_straight_flush(hand):
    if check_flush(hand) and check_straight(hand):
        return True
    else:
        return False


def check_four_of_a_kind(hand):
    values = [i[0] for i in hand]
    value_counts = defaultdict(lambda: 0)
    for v in values:
        value_counts[v] += 1
    if sorted(value_counts.values()) == [1, 1, 1, 4]:
        return True
    elif sorted(value_counts.values()) == [1, 2, 4]:
        return True
    elif sorted(value_counts.values()) == [3, 4]:
        return True
    else:
        return False


def check_full_house(hand):
    values = [i[0] for i in hand]
    value_counts = defaultdict(lambda: 0)
    for v in values:
        value_counts[v] += 1
    if sorted(value_counts.values()) == [1, 1, 2, 3]:
        return True
    elif sorted(value_counts.values()) == [1, 3, 3]:
        return True
    elif sorted(value_counts.values()) == [2, 2, 3]:
        return True
    else:
        return False


def check_flush(hand):
    suits = [i[1] for i in hand]
    if len(set(suits)) == 1:
        return True
    else:
        return False


def check_straight(hand):
    values = [i[0] for i in hand]
    rank_values = [card_order_dict[i] for i in values]
    rank_values.sort()
    if rank_values[4]-rank_values[3] == 1 and rank_values[3]-rank_values[2] == 1 and rank_values[2]-rank_values[1] == 1 and rank_values[1]-rank_values[0] == 1:
        return True
    elif rank_values[5]-rank_values[4] == 1 and rank_values[4]-rank_values[3] == 1 and rank_values[3]-rank_values[2] == 1 and rank_values[2]-rank_values[1] == 1:
        return True
    elif rank_values[6]-rank_values[5] == 1 and rank_values[5]-rank_values[4] == 1 and rank_values[4]-rank_values[3] == 1 and rank_values[3]-rank_values[2] == 1:
        return True
    else:
        return False


def check_three_of_a_kind(hand):
    values = [i[0] for i in hand]
    value_counts = defaultdict(lambda: 0)
    for v in values:
        value_counts[v] += 1
    if sorted(value_counts.values()) == [1, 1, 1, 1, 3]:
        return True
    else:
        return False


def check_two_pairs(hand):
    values = [i[0] for i in hand]
    value_counts = defaultdict(lambda: 0)
    for v in values:
        value_counts[v] += 1
    if sorted(value_counts.values()) == [1, 1, 1, 2, 2]:
        return True
    else:
        return False


def check_one_pairs(hand):
    values = [i[0] for i in hand]
    value_counts = defaultdict(lambda: 0)
    for v in values:
        value_counts[v] += 1
    if 2 in value_counts.values():
        return True
    else:
        return False


def check_high_card(hand):
    values = [i[0] for i in hand]
    value_counts = defaultdict(lambda: 0)
    for v in values:
        value_counts[v] += 1
    rank_values = [card_order_dict[i] for i in values]
    return max(rank_values)


print(score_my_hand(['5C', '6H', '4C', 'AS', '7C', '8H', 'AD']))
