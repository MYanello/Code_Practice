#!/usr/bin/env python
from icecream import ic
import regex as re

def hash(string):
    hashed = 0
    for char in string:
        hashed += ord(char)
        hashed *= 17
        hashed %= 256
    return hashed
    
def parser(file):
    with open(file, 'r') as f:
        data = [line.strip() for line in f.readlines()]
        data = re.split(r'\,', data[0])
    return data

def main(file):
    data = parser(file)
    summed = 0
    for string in data:
        summed += hash(string)
    return summed
    
if __name__ == '__main__':
    assert hash('HASH') == 52
    assert main('test.txt') == 1320
    ic(main('input.txt'))