#!/usr/bin/env python3
from icecream import ic
import regex as re

def parser(file):
    with open(file, 'r') as f:
        data = f.read()
    data = data.split('\n')
    data = [line.split(' ') for line in data]
    directions = data[0]
    directions = re.findall(r'.', directions[0])
    mapp = data[2:]
    map_dict = {}
    start_position = mapp[0][0]
    for line in mapp:
        line.pop(1)
        line[1] = re.sub(r'(\()|(\,)', '', line[1], count=2)
        line[2] = re.sub(r'\)', '', line[2], count=2)
        map_dict[line[0]] = line[1:]
    return directions, map_dict, start_position

def route(directions, mapp, start_position):
    location = start_position
    i = 0
    loop = 0
    while location != 'ZZZ':
        if i >= len(directions):
            i = 0
            loop += 1
        l_or_r = directions[i]
        if l_or_r == 'L':
            location = mapp[location][0]
            ic(location)
        elif l_or_r == 'R':
            location = mapp[location][1]
            ic(location)
        i += 1
    return (i + (loop * len(directions)))


if __name__ == '__main__':
    directions, mapp, start_position = parser('input.txt')
    ic(directions)
    ic(mapp)
    ic(start_position)
    ic(route(directions, mapp, start_position))