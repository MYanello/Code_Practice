#!/usr/bin/env python3
from icecream import ic
import regex as re

def lotto(file):
    win_nums = []
    my_nums = []
    with open(file) as f:
        lines = f.readlines()
        score = 0
        for line in lines:
            matches = 0
            card_score = 0
            #ic(line)
            card = re.split(r'\:|\|',line)
            #ic(card)
            win_nums = card[1].strip()
            win_nums = re.split(r'\ ',win_nums)
            win_nums = list(filter(None, win_nums))
            my_nums = card[2].strip()
            my_nums = re.split(r'\ ',my_nums)
            my_nums = list(filter(None, my_nums))
            ic(win_nums)
            ic(my_nums)
            for num in my_nums:
                if num in win_nums:
                    matches += 1
            ic(matches)
            if matches == 0:
                card_score = 0
            elif matches == 1:
                card_score = 1
            else:
                card_score = 1
                while matches > 1:
                    card_score *= 2
                    matches -= 1
            ic(card_score)
            score += card_score
            ic(score)
    return score

def lotto2(file):
    win_nums = []
    my_nums = []
    with open(file) as f:
        lines = f.readlines()
        cards_count = [1] * len(lines)
        ic(cards_count)
        for line in lines:
            card = re.split(r'\:|\|',line)
            win_nums = card[1].strip()
            win_nums = re.split(r'\ ',win_nums)
            win_nums = list(filter(None, win_nums))
            my_nums = card[2].strip()
            my_nums = re.split(r'\ ',my_nums)
            my_nums = list(filter(None, my_nums))
        for i in range(len(lines)): # for each card i
            ic(i)
            ic(cards_count[i])
            ic(range(cards_count[i]))
            for j in range(cards_count[i]): # for each copy of the card j 
                ic(j)
                k = 0 # each run of each copy
                for num in my_nums[i]: # for each number in the card
                    ic(num)
                    if num in win_nums[i]:
                        ic('Matched')
                        cards_count[i+k] += 1 # increase the next card count by 1 for each match
                        ic(cards_count)
                        k +=1
                

if __name__ == '__main__':
    ic.disable()
    assert lotto('test.txt') == 13
    #print(lotto('test.txt'))
    #print(lotto('input.txt'))
    ic.enable()
    print(lotto2('test.txt'))
