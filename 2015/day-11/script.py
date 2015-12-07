#!/usr/bin/env python

def position(character):
    return (ord(character) - ord('a')) % 26

def character(position):
    return chr(position + ord('a'))

def increment(positions):
    new_positions = []

    carry = True
    for pos in reversed(positions):
        new_pos = (pos + 1) % 26 if carry else pos
        carry = carry and (new_pos == 0)        
        new_positions.insert(0, new_pos)

    return new_positions

def next(line):
    positions = list(map(position, line))
    next_line = list(map(character, increment(positions)))
    return ''.join(next_line)

def has_increasing_straight(line, i):
    if (i + 2) >= len(line):
        return False

    p1 = ord(line[i])
    p2 = ord(line[i + 1])
    p3 = ord(line[i + 2])
    return (p3 - p2) == 1 and (p2 - p1) == 1

def is_password(line):
    pairs = set()
    increasing_straight = False

    for i in range(len(line)):
        if line[i] in { 'i', 'o', 'l' }:
            return False

        if not increasing_straight:
            increasing_straight = has_increasing_straight(line, i)

        if (i + 1) != len(line) and line[i] == line[i + 1]:
            pairs.add(line[i] + line[i + 1])
        
    return increasing_straight and len(pairs) >= 2

def search_next_password(password):
    cpt = 1
    p = next(password)
    while not is_password(p):
        p = next(p)

        cpt += 1
        if cpt % 100000 == 0:
            print('Processed 100000 strings so far...')

    return p

puzzle = search_next_password('hepxcrrq')
print('Next password is', puzzle)

puzzle = search_next_password(puzzle)
print('Next password is', puzzle)
