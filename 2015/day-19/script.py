#!/usr/bin/env python

import re

def parse_replacements():
    replacements = set()
    molecule = ''

    f = open('data')
    for l in f:
        line = l.replace('\n', '')

        m = re.match(r'(\w+) => (\w+)', line)
        if m:
            replacements.add(( m.group(1), m.group(2) ))
        else:
            molecule = line

    return (molecule, replacements)

def nb_of_replaced_molecules(molecule, replacements):
    replaced_molecules = set()
    for old, new in replacements:
        for m in re.finditer(old, molecule):
            i = m.start() # index at which we must replace
            replaced = molecule[:i] + new + molecule[i + len(old):]
            replaced_molecules.add(replaced)

    return len(replaced_molecules)

def min_steps(molecule):
    n_tokens = len(re.findall(r'[A-Z][a-z]?', molecule))
    n_Rn_or_Ar = len(re.findall(r'(Rn)|(Ar)', molecule))
    n_Y = len(re.findall(r'Y', molecule))

    return n_tokens - n_Rn_or_Ar - 2 * n_Y - 1

if __name__ == '__main__':
    molecule, replacements = parse_replacements()
    n = nb_of_replaced_molecules(molecule, replacements)
    print('[Part 1] number of possible replacements:', n)

    print('[Part 2] lowest number of steps:', min_steps(molecule))
