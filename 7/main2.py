#!/usr/bin/env python3
from icecream import ic
import regex as re

# j are now wildcards but worth 1:

strength = {
    'T': '10',
    'J': '1',
    'Q': '12',
    'K': '13',
    'A': '14'
}


def check_hand_mapping(hand):
    hand = re.findall(r'.', hand)
    hand_map = {}
    for card in hand:
        #ic(hand_map)
        if not card in hand_map:
            hand_map[card] = 0
        if card in hand_map:
            hand_map[card] += 1
    if 'J' in hand_map:
        jokers = hand_map['J']
        ic(jokers)
    return hand_map

def check_hand_type(hand_mapping):
    if check_five_of_a_kind(hand_mapping):
        return 'five_of_a_kind'
    if check_four_of_a_kind(hand_mapping):
        return 'four_of_a_kind'
    if check_full_house(hand_mapping):
        return 'full_house'
    if check_three_of_a_kind(hand_mapping):
        return 'three_of_a_kind'
    if check_two_pairs(hand_mapping):
        return 'two_pairs'
    if check_one_pair(hand_mapping):
        return 'one_pair'
    return 'high_card'

def check_hand_score(type):
    type_value = {
    'five_of_a_kind': 7,
    'four_of_a_kind': 6,
    'full_house': 5,
    'three_of_a_kind': 4,
    'two_pairs': 3,
    'one_pair': 2,
    'high_card': 1
    }
    return type_value[type]

def check_five_of_a_kind(hand_mapping):
    for card in hand_mapping:
        if hand_mapping[card] == 5:
            return True
    return False
def check_four_of_a_kind(hand_mapping):
    for card in hand_mapping:
        if hand_mapping[card] == 4:
            return True
    return False
def check_full_house(hand_mapping):
    three_of_a_kind = False
    two_of_a_kind = False
    for card in hand_mapping:
        if hand_mapping[card] == 3:
            three_of_a_kind = True
        if hand_mapping[card] == 2:
            two_of_a_kind = True
    if three_of_a_kind and two_of_a_kind:
        return True
    return False
def check_three_of_a_kind(hand_mapping):
    for card in hand_mapping:
        if hand_mapping[card] == 3:
            return True
    return False
def check_two_pairs(hand_mapping):
    pairs = 0
    for card in hand_mapping:
        if hand_mapping[card] == 2:
            pairs += 1
    if pairs == 2:
        return True
    return False
def check_one_pair(hand_mapping):
    for card in hand_mapping:
        if hand_mapping[card] == 2:
            return True
    return False

def parser(file):
    with open(file, 'r') as f:
        data = f.read()
    data = data.split('\n')
    data = [line.split(' ') for line in data]
    return data

def tiebreaker_value(data):
    for player in data:
        hand = player[0]
        tiebreaker = []
        for card in hand:
            if card in strength:
                player.append(int(strength[card]))
            else:
                player.append(int(card))
    return data

def add_score_to_player(data):
    for player in data:
        ic(player[0])
        hand_mapping = check_hand_mapping(player[0])
        ic(hand_mapping)
        hand_type = check_hand_type(hand_mapping)
        ic(hand_type)
        hand_score = check_hand_score(hand_type)
        ic(hand_score)  
        player.append(hand_score)
    return data

def sort_scores(data):
    sorted_data = sorted(data, key=lambda x: x[2:], reverse=False)
    return sorted_data

def count_winnings(data):
    score = 0
    for i, player in enumerate(data):
        ic(player)
        ic(player[2])
        ic(i)
        player.append(int(player[1])*(i+1))
        score += (int(player[1])*(i+1))
    return (data, score)

if __name__ == '__main__':
    data = parser('test.txt')
    add_score_to_player(data)
    tiebreaker_value(data)
    data = sort_scores(data)
    ic.enable()
    data, score = count_winnings(data)
    ic(data)
    ic(score)
