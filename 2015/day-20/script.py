#!/usr/bin/env python

def find_lowest_id(target, elf_factor, elf_visits = None):
    max_id = target // elf_factor
    houses = [ 0 for house_id in range(max_id + 1) ]
    # houses is of size max_id + 1 to start indexes at 1.

    for elf_id in range(1, max_id + 1):

        capped_max = max_id
        if elf_visits is not None:
            capped_max = min(max_id, elf_visits * elf_id)

        for house_id in range(elf_id, capped_max + 1, elf_id):
            houses[house_id] += elf_id * elf_factor

    return min_index(houses, target)

def min_index(houses, target):
    for i in range(1, len(houses)):
        if houses[i] >= target:
            return i

    return -1

if __name__ == '__main__':

    lowest_id = find_lowest_id(33100000, 10)
    print('Part 1: house id is:', lowest_id)

    lowest_id = find_lowest_id(33100000, 11, 50)
    print('Part 2: house id is:', lowest_id)
