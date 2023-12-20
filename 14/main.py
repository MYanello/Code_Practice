#!/usr/bin/env python
from icecream import ic
import regex as re

def shift_north(data):
    run = 1
    while run > 0:
        run -= 1
        for i, line in enumerate(data):  # row
            for j, char in enumerate(line):  # column
                if char == 'O':
                    if i > 0 and data[i - 1][j] == '.':
                        data[i - 1][j] = 'O'
                        data[i][j] = '.'
                        run += 1
    return data

def shift_east(data):
    run = 1
    while run > 0:
        run -= 1
        for i, line in enumerate(data):  # row
            for j, char in enumerate(line):  # column
                if char == 'O':
                    if i > 0 and data[i][j + 1] == '.':
                        data[i][j + 1] = 'O'
                        data[i][j] = '.'
                        run += 1
    return data

def shift_south(data):
    run = 1
    while run > 0:
        run -= 1
        for i, line in enumerate(data):  # row
            for j, char in enumerate(line):  # column
                if char == 'O':
                    if i > 0 and i < len(data) - 1 and j > 0 and j < len(data) - 1 and data[i + 1][j] == '.':
                        data[i + 1][j] = 'O'
                        data[i][j] = '.'
                        run += 1
    return data

def shift_west(data):
    run = 1
    while run > 0:
        run -= 1
        for i, line in enumerate(data):  # row
            for j, char in enumerate(line):  # column
                if char == 'O':
                    if i > 0 and i < len(data) and j < len(line) - 1 and data[i][j + 1] == '.':
                        data[i][j - 1] = 'O'
                        data[i][j] = '.'
                        run += 1
    return data

def cycle(data):
    data = shift_north(data)
    data = shift_west(data)
    data = shift_south(data)
    data = shift_east(data)
    return data

def parser(file):
    with open(file, 'r') as f:
        data = [line.strip() for line in f.readlines()]
        data = [re.split(r' ',line) for line in data]
        out = []
        for line in data:
            chars = [char for char in line[0]]
            out.append(chars)
    return out

def calc_load(data):
    load = 0
    for i, line in enumerate(data):
        force = len(data) - i #len = 10. when i = 0, force = 10; i = 9, force = 1
        load += line.count('O') * force
    return load

def pt1(input):
    data = parser(input)
    northern = shift_north(data)
    load = calc_load(northern)
    return load

def pt2(input, cycles):
    data = parser(input)
    for _ in range(cycles):
        data = cycle(data)
    load = calc_load(data)

if __name__ == '__main__':
    assert pt1('test.txt') == 136
    #ic(pt1('input.txt'))
    ic(pt2('test.txt', 3))