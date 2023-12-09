#!/usr/bin/env python
from icecream import ic
import regex as re
import numpy as np

def find_next(data):
    left_predict, right_predict = 0, 0
    for line in data:
        right_predict += right_history(line)
        left_predict += left_history(line)
    ic(left_predict)
    return left_predict

def right_history(line):
    line = np.array(line)
    next_line = line
    arr = [line.tolist()]
    while not np.all(next_line == 0):
        next_line = np.diff(next_line)
        arr.append(next_line.tolist())
    next = 0
    arr.reverse()
    for line in arr:
        next = line[-1] + next
    return(next)

def left_history(line):
    line = np.array(line)
    next_line = line
    arr = [line.tolist()]
    while not np.all(next_line == 0):
        next_line = np.diff(next_line)
        arr.append(next_line.tolist())
    arr.reverse() 
    ic(arr)
    for i, line in enumerate(arr):
        ic(len(arr))
        ic(i-1)
        if i == len(arr)-1:
            next_num = arr[i][0]
        else:
            next_num = arr[i+1][0]
        # next_num = arr[i+1][0]
        curr = line[0]
        ic(next_num, curr)
        if i == len(arr)-1:
            arr[i][0] = next_num
        else:
            arr[i+1][0] = next_num - curr
    return(next_num)

def parser(file):
    with open(file, 'r') as f:
        data = []
        for line in f.readlines():
            line = line.strip()
            line = re.split(r'\s+', line)
            for i in range(len(line)):
                line[i] = int(line[i])
            #ic(line)
            data.append(line)
    return data

if __name__ == '__main__':
    ic.disable()
    data = parser('input.txt')
    print(find_next(data))