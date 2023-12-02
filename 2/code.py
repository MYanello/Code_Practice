#!/usr/bin/env python3
from icecream import ic
import pandas as pd
import regex as re

def games(file):
    max = {
        "red": 12,
        "green": 13,
        "blue": 14
    }
    with open(file) as f:
        ic.disable()
        lines = f.readlines()
        colors = []
        for line in lines:
            ic(line)
            game, color_data = line.split(':')
            colors.append(color_data.strip())
        #ic.enable()
        game_num = 0
        sum = 0
        pattern = re.compile(r'(\d+)\s(red|green|blue)')
        for game in colors:
            game_num += 1
            ic(game)
            game = game.split(';')
            possible_game = True
            for subset in game:
                matches = pattern.findall(subset)
                ic(matches)
                result = {'red': 0, 'green': 0, 'blue': 0}
                for count, color in matches:
                    result[color] += int(count)
                    ic(result)
                if result['red'] > max['red'] or result['green'] > max['green'] or result['blue'] > max['blue']:
                    possible_game = False
                    break
            if possible_game:
                ic(game_num)
                sum += game_num
            ic(sum)
        return sum

def games2(file):
    with open(file) as f:
        ic.disable()
        lines = f.readlines()
        colors = []
        for line in lines:
            game, color_data = line.split(':')
            colors.append(color_data.strip())
        pattern = re.compile(r'(\d+)\s(red|green|blue)')
        total = 0
        for game in colors:
            game = game.split(';')
            result = {'red': 0, 'green': 0, 'blue': 0}
            for subset in game:
                matches = pattern.findall(subset)
                for count, color in matches:
                    if result[color] < int(count):
                        result[color] = int(count)
            ic(result)
            power = result['red'] * result['green'] * result['blue']
            total += power
            ic(total)
        return total
if __name__ == '__main__':
    assert games('testinput.txt') == 8
    print(games('input.txt'))
    assert games2('testinput.txt') == 2286
    print(games2('input.txt'))