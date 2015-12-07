#!/usr/bin/env python

def find_combinations(remaining_sizes, total_size, combinations, current_combination = []):
    if total_size < 0:
        return # Backtracking

    if not total_size:
        combinations.append(current_combination)
        return # Backtracking

    if not remaining_sizes:
        return # Backtracking

    sizes = remaining_sizes.copy()
    size  = sizes.pop()

    find_combinations(sizes, total_size, combinations, current_combination)
    find_combinations(sizes, total_size - size, combinations, current_combination + [ size ])

def nb_of_minimum_combinations(combinations):
    minimum_length = min(map(lambda c: len(c), combinations))
    return len(list(filter(lambda c: len(c) == minimum_length, combinations)))

if __name__ == '__main__':

    container_sizes = []

    f = open('data')
    for line in f:
        container_sizes.append(int(line))
    f.close()

    all_combinations = []
    find_combinations(container_sizes, 150, all_combinations)

    print('[Part 1]: There are', len(all_combinations), 'combinations.')
    print('[Part 2]: There are', nb_of_minimum_combinations(all_combinations), 'combinations.')
