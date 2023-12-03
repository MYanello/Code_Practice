#!/usr/bin/env python3
from icecream import ic
import regex as re

def parts1(file):
    numbersmap = re.compile(r'(\d+)')
    symbolsmap = re.compile(r'(\*|\!|\#|\@|\$|\%|\^|\&|\=|\/|\\|\+)')
    with open(file) as f:
        lines = f.read().splitlines()
        i = 0
        total = 0
        #ic(len(lines))
        for line in lines:
            if i != 0:
                ic.disable()
            parts = numbersmap.finditer(line)
            for obj in parts:
                ic(lines[i-1])
                ic(line)
                #ic(lines[i+1])
                ic(obj.group())
                #ic.disable()
                adjacent = []
                start_location = obj.start()
                if start_location == 0: # first character in line
                    start_location = 1
                end_location = obj.end()
                if end_location == len(line): # last character in line
                    end_location = len(line)-1
                adjacent.append(line[start_location-1])
                adjacent.append(line[end_location])
                #ic(i)                
                if i == 0: # first line
                    ic(lines[i+1][start_location-1:end_location+1])
                    adjacent.append(lines[i+1][start_location-1:end_location+1])                
                elif i == len(lines)-1: # last line
                    adjacent.append(lines[i-1][start_location-1:end_location+1])
                else:
                    adjacent.append(lines[i-1][start_location-1:end_location+1])
                    adjacent.append(lines[i+1][start_location-1:end_location+1])
                adjacent = ''.join(adjacent)
                ic(adjacent)
                if symbolsmap.search(adjacent):
                    ic('Part')
                    total += int(obj.group())
                    ic(total)
            i += 1
    return total

if __name__ == '__main__':
    #assert parts1('test.txt') == 4361
    print(parts1('test.txt'))
    #ic.disable()
    #print(parts1('input.txt'))