#!/usr/bin/env python
from icecream import ic
import numpy as np
import regex as re

def parser(file):
    with open(file, 'r') as f:
        data = [line.strip() for line in f.readlines()]
        data = [re.split(r' ',line) for line in data]
        maps = [line[0] for line in data]
        counts = [line[1] for line in data]
    return maps, counts

if __name__ == '__main__':
    maps, counts = parser('test.txt')
    ic(maps, counts)
    