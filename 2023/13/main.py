#!/usr/bin/env python
from icecream import ic
import numpy as np
import regex as re

def parser(file):
    with open(file, 'r') as f:
        data = [line.strip() for line in f.readlines()]
        data = [re.split(r' ',line) for line in data]
    return data

if __name__ == '__main__':
    parser(test.txt)
    print(True)
