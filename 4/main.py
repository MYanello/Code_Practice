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

if __name__ == '__main__':
    assert lotto('test.txt') == 13
    print(lotto('test.txt'))
    print(lotto('input.txt'))
