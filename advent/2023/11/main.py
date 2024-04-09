#!/usr/bin/env python3
from icecream import ic
import numpy as np

def parser(file):
    with open(file, 'r') as f:
        data = np.array([list(line.strip()) for line in f.readlines()])
    return data

def expand_rows(data):
    for i, line in enumerate(data):
        for j, char in enumerate(line)
            if '#' in line:
                
            

if __name__ == '__main__':
   data = parser('test.txt')
   ic(data)