#!/usr/bin/env python
from icecream import ic

pipes = {
    '|': ['N', 'S'],
    '-': ['E', 'W'],
    'L': ['N', 'E'],
    'J': ['N', 'W'],
    '7': ['S', 'W'],
    'F': ['S', 'E'],
    'S': ['N', 'S', 'E', 'W']
}

connected_pipes = {
    'N': 'i+1',
    'S': 'i-1',
    'E': 'j+1',
    'W': 'j-1'
}

pipes2 = {
    '|': [['i+1','j'], ['i-1','j']],
    '-': [['i','j+1'], ['i','j-1']],
    'L': [['i-1','j'], ['i','j+1']],
    'J': [['i-1','j'], ['i','j-1']],
    '7': [['i+1','j'], ['i','j-1']],
    'F': [['i+1','j'], ['i-1','j']],
    'S': [['i+1','j'], ['i-1','j'], ['i', 'j-1'], ['i', 'j+1']]
}

class pipe:
    def __init__(self, data, posi, posj,):
        self.type = data[posi][posj]
        self.pipes_shapes = {
            '|': ['N', 'S'],
            '-': ['E', 'W'],
            'L': ['N', 'E'],
            'J': ['N', 'W'],
            '7': ['S', 'W'],
            'F': ['S', 'E'],
            'S': ['N', 'S', 'E', 'W'],
            '.': ['.']
        }
        try:
            self.n = self.pipes_shapes[data[posi-1][posj]]
        except:
            self.n = '.'
        try:
            self.s = self.pipes_shapes[data[posi+1][posj]]
        except:
            self.s = '.'
        try:
            self.e = self.pipes_shapes[data[posi][posj+1]]
        except:
            self.e = '.'
        try:
            self.w = self.pipes_shapes[data[posi][posj-1]]
        except:
            self.w = '.'
    def check_north(self):
        try:
            if 'S' in self.n:
                ic('Connected north')
                return True
        except:
            return False
    def check_south(self):
        try:
            if 'N' in self.s:
                ic('Connected south')
                return True
        except:
            return False
    def check_east(self):
        try:
            if 'W' in self.e:
                ic('Connected east')
                return True
        except:
            return False
    def check_west(self):
        try:
            if 'E' in self.w:
                ic('Connected west')
                return True
        except:
            return False
    def checks(self):
        match self.type:
            case '.':
                return False
            case '|':
                if self.check_north() and self.check_south():
                    ic('Connected pipes')
                    return True
            case '-':
                ic('Checking -')
                if self.check_east() and self.check_west():
                    ic('Connected pipes')
                    return True
            case 'L':
                if self.check_north() and self.check_east():
                    ic('Connected pipes')
                    return True
            case 'J':
                if self.check_north() and self.check_west():
                    ic('Connected pipes')
                    return True
            case '7':
                ic('Checking 7')
                if self.check_south() and self.check_west():
                    ic('Connected pipes')
                    return True
            case 'F':
                if self.check_east() and self.check_south():
                    ic('Connected pipes')
                    return True
            case 'S':
                ic('Connected pipes')
                return True
            case _:
                ic('Pipe type not matched')
                return False

def main_loop(data):
    for i, line in enumerate(data):
        for j, char in enumerate(line):
            ic(char, i, j)
            this_char = pipe(data, i, j)
            ic(this_char.type)
            ic(this_char.checks())
            if not this_char.checks():
                ic('Pipe not connected')
                data[i][j] = '.'
    ic.enable()
    ic(data)
    return data

def parser(file):
    with open(file, 'r') as f:
        lines = f.readlines()
    data = [list(line.strip()) for line in lines]
    ic(data)
    return data

if __name__ == '__main__':
    ic.disable()
    data = parser('input.txt')
    main_loop = main_loop(data)
    pipes = 0
    for line in main_loop:
        for char in line:
            if char != '.':
                pipes +=1
    print(pipes)
    