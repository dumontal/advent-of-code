#!/usr/bin/env python

import re, sys, itertools, functools

def parse_line(line):
    m = re.match(r'(\w+) would (\w+) (\d+) happiness units by sitting next to (\w+).', line)
    happiness = int(m.group(3))
    if m.group(2) == 'lose':
        happiness = - happiness

    return ( m.group(1), happiness, m.group(4) )

def happiness(name_1, name_2, prefs):
    for pref in prefs:
        if (name_1 == pref[0]) and (name_2 == pref[2]):
            return pref[1]

    print('Failed to find happiness between', name_1, 'and', name_2)
    sys.exit(1)

def compute_happiness(arr, prefs):
    total_happiness = 0
    for j in range(len(arr)):
        i = j - 1 if j > 0 else len(arr) - 1
        k = j + 1 if j < len(arr) - 1 else 0

        total_happiness += happiness(arr[j], arr[i], prefs)
        total_happiness += happiness(arr[j], arr[k], prefs)

    return total_happiness

def optimal_happiness(names, prefs):
    compute = lambda arr: compute_happiness(arr, prefs)
    return max(map(compute, itertools.permutations(names)))

if __name__ == '__main__':
    guys = set()
    preferences = set()

    f = open('data')
    for line in f:
        pref = parse_line(line)

        guys.add(pref[0])
        guys.add(pref[2])
        preferences.add(pref)

    f.close()

    print('(Part 1) Optimal happiness change is', optimal_happiness(guys, preferences))

    myself = 'dumontal' # Should be a name not in `guys`.
    for guy in guys:
        preferences.add(( myself, 0, guy ))
        preferences.add(( guy, 0, myself ))

    guys.add(myself)

    print('(Part 2) Optimal happiness change is', optimal_happiness(guys, preferences))
