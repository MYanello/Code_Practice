#!/usr/bin/env python3
from icecream import ic
import numpy as np

def ways_to_win(races):
    all_ways = np.array([])
    for race in races:
        ways_to_win = 0
        ic(race)
        time, distance = race[0], race[1]
        for hold_time in range(time):
            speed = hold_time
            ic(hold_time)
            time_left = time - hold_time
            distance_travelled = time_left * speed
            ic(distance_travelled)
            if distance_travelled > distance:
                ways_to_win += 1
                ic(True)
        all_ways = np.append(all_ways, ways_to_win)
    return all_ways


if __name__ == '__main__':
    print(0)
    test_cases = [[7, 9], [15, 40], [30, 200]]
    cases = [[48, 296], [93, 1928], [85, 1236], [95, 1391]]
    test_cases2 = [[71530, 94020]]
    cases_2 = [[48938595, 296192812361391]]
    #ic(np.prod(ways_to_win(test_cases)))
    #ic(np.prod(ways_to_win(cases)))
    ic.disable()
    # a more graceful way to do this would be to find for the minimum and maximum hold time and then factorial it up.
    print(np.prod(ways_to_win(test_cases2)))
    print(np.prod(ways_to_win(cases_2)))