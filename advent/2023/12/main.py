#!/usr/bin/env python
from icecream import ic
import numpy as np
import regex as re

class row:
    def __init__(self, data):
        self.mapp = data[0]
        self.counts = (data[1].split(','))
        self.counts = [int(count) for count in self.counts]
        ic(self.mapp, self.counts)
        self.grouping = [x for x in re.split(r'\.+', self.mapp) if x]
        ic(self.grouping)

    def get_poss(self):
        poss = 0
        for i, set in enumerate(self.grouping):
            if '?' in set:
                poss += int(self.counts[i]) % set.count('?')
                ic(set.count('?'), self.counts[i], set)
                ic(poss)

def parser(file):
    with open(file, 'r') as f:
        data = [line.strip() for line in f.readlines()]
        data = [re.split(r' ',line) for line in data]
    return data

if __name__ == '__main__':
    data = parser('test.txt')
    ic(data[1])
    row1 = row(data[1])
    row1.get_poss()
