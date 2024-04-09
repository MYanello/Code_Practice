#!/usr/bin/env python3
from icecream import ic
import regex as re
'''
Combine first digit and last digit to form single two digit number then sum them all
in:
1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet
out:
12
38
15
77
=142
'''
ic.disable()
testdata1 = [
    "1abc2",
    "pqr3stu8vwx",
    "a1b2c3d4e5f",
    "treb7uchet"
    ]
def decode(data):
    running = 0
    for line in data:
        chars = line.split()
        chars = str(chars[0])
        #ic(chars)
        digits = []
        for char in chars:
            ic(char.isdigit())
            if char.isdigit():
                digits.append(char)
                ic(digits)
        combined = digits[0] + digits[-1]
        ic(combined)
        running += int(combined)
        ic(running)
    return running

testdata2 = [
    "two1nine",
    "eightwothree",
    "abcone2threexyz",
    "xtwone3four",
    "4nineeightseven2",
    "zoneight234",
    "7pqrstsixteen"
]

def decode2(data):
    num_map = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five" : 5,
    "six" : 6,
    "seven" : 7,
    "eight" : 8,
    "nine" : 9
    }
    running = 0
    for line in data:
        digits = re.findall(r'\d|zero|one|two|three|four|five|six|seven|eight|nine', line, overlapped=True)
        for i in range(len(digits)):
            if digits[i].isnumeric() == False:
                digits[i] = num_map.get(digits[i])
        code = str(digits[0]) + str(digits[-1])
        running += int(code)
    return running

if __name__ == "__main__":
    test = decode(testdata1)
    print(f"Test result: {test}")

    with open('input.txt', 'r') as f:
        data = f.readlines()
        result = decode(data)
        print(f"Result: {result}")

    test2 = decode2(testdata2)
    print(f"Test2 result: {test2}")
    with open('input.txt', 'r') as f:
        data = f.readlines()
        result = decode2(data)
        print(f"Result: {result}")
