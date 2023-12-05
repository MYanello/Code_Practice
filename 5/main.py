#!/usr/bin/env python3
from icecream import ic
import regex as re

class mapping:
    def __init__(self, name, values):
        self.name = name
        self.values = values
        self.dest, self.src, self.range = [], [], []
        for line in self.values:
            self.dest.append(line[0])
            self.src.append(line[1])
            self.range.append(line[2])
    def find_next_val(self, value):
        next_value = None
        for i in range(len(self.src)):
            src_lower_lim = self.src[i]
            ic(src_lower_lim)
            src_upper_lim = self.src[i] + self.range[i]
            ic(src_upper_lim)
            if value in range(src_lower_lim, src_upper_lim):
                next_value = value - src_lower_lim + self.dest[i]
                ic(value)
                ic(self.dest[i])
                ic(self.src[i])
                ic(next_value)
                break
        if not next_value:
            next_value = value
        return next_value      
    def info(self):
        ic('Details:')
        ic(self.name)
        ic(self.values)

def parser(file):
    with open(file) as f:
        maps = {}
        curr_map = None
        lines = f.readlines()
        seeds = re.split(r'\ | \:',(lines[0].strip()))
        seeds = seeds[1:]
        for i in range(len(seeds)):
            seeds[i] = int(seeds[i])
        rest = lines[2:]
        for line in rest:
            line = line.strip('\n')
            if line.endswith('map:'):
                curr_map = line[:-5].replace('-','_')
                maps[curr_map] = []
            elif line:
                values = list(map(int, line.split()))
                maps[curr_map].append(values)
        return seeds, maps


def location(seeds, maps):
    ic(seeds)
    ic(maps)
    for map_name, value_list in maps.items():
        globals()[map_name] = mapping(name = map_name, values = value_list)
    locations = []
    for seed in seeds:
        #seed = 14
        ic.disable()
        ic(seed)
        soil = seed_to_soil.find_next_val(seed)
        ic(soil)
        fertil = soil_to_fertilizer.find_next_val(soil)
        ic(fertil)
        water = fertilizer_to_water.find_next_val(fertil)
        ic(water)
        light = water_to_light.find_next_val(water)
        ic(light)
        temp = light_to_temperature.find_next_val(light)
        ic(temp)
        humid = temperature_to_humidity.find_next_val(temp)
        ic(humid)
        loc = humidity_to_location.find_next_val(humid)
        ic.enable()
        ic(loc)
        locations.append(loc)
        print(f'\n')
    return min(locations)

def seed_range(seeds):
    i = 0
    seeds_2 = []
    while i < len(seeds):
        ic(seeds[i])
        ic(seeds[i+1])
        seed_start = seeds[i]
        seed_end = seeds[i] + seeds[i+1]-1
        i += 2
        ic(seed_start)
        ic(seed_end)
        seeds_2.append(list(range(seed_start, seed_end)))
        # for j in range(seed_start, seed_end):
        #     seeds_2.append(j)
    return (seeds_2)



if __name__ == '__main__':
    #seeds, maps = parser('test.txt')
    #ic(seeds)
    #seeds_2 = seed_range(seeds)
    #print(location(seeds, maps))
    #print(location(seeds_2, maps))
    seeds, maps = parser('input.txt')
    #print(location(seeds, maps))
    seeds_2 = seed_range(seeds)
    print(location(seeds_2, maps))
