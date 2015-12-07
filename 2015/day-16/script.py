#!/usr/bin/env python

import re

def parse(line):
    m = re.match(r'Sue (\d+):(.*)\n', line)

    compounds = dict()
    for compound_str in m.group(2).split(','):
        sm = re.match(r' (\w+): (\d+)', compound_str)
        compounds.update({ sm.group(1) : int(sm.group(2)) })

    return { int(m.group(1)) : compounds }

def checker_v1(compound, quantity, ref):
    return ref[compound] == quantity

def checker_v2(compound, quantity, ref):
    if compound in ( 'cats', 'trees' ):
        return ref[compound] < quantity

    if compound in ( 'pomeranians', 'goldfish' ):
        return ref[compound] > quantity

    return checker_v1(compound, quantity, ref)

def find_candidates(aunts_with_compounds, ref, checker):
    candidates = list()
    for aunt, compounds in aunts_with_compounds.items():
        
        is_candidate = True
        for compound, quantity in compounds.items():
            if not checker(compound, quantity, ref):
                is_candidate = False
                break

        if is_candidate:
            candidates.append(aunt)

    return candidates

if __name__ == '__main__':
    
    aunts = dict()
    reference = {
        'children'   : 3,
        'cats'       : 7,
        'samoyeds'   : 2,
        'pomeranians': 3,
        'akitas'     : 0,
        'vizslas'    : 0,
        'goldfish'   : 5,
        'trees'      : 3,
        'cars'       : 2,
        'perfumes'   : 1
    }

    f = open('data')
    for line in f:
        aunts.update(parse(line))

    f.close()

    print('[Part 1] Candidates are:', find_candidates(aunts, reference, checker_v1))
    print('[Part 2] Candidates are:', find_candidates(aunts, reference, checker_v2))
