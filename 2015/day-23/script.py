#!/usr/bin/env python

import re

def parse(line):
    m = re.match(r'(hlf|tpl|inc) (a|b)', line)
    if m:
        return m.group(1), m.group(2)

    m = re.match(r'(jmp) (\+?\-?\d+)', line)
    if m:
        return m.group(1), int(m.group(2))

    m = re.match(r'(jie|jio) (a|b), (\+?\-?\d+)', line)
    if m:
        return m.group(1), m.group(2), int(m.group(3))

    return 'not decoded'

def hlf(inst, a, b, pc):
    if inst[1] == 'a':
        a //= 2
    elif inst[1] == 'b':
        b //= 2
    
    return a, b, pc + 1

def tpl(inst, a, b, pc):
    if inst[1] == 'a':
        a *= 3
    elif inst[1] == 'b':
        b *= 3

    return a, b, pc + 1

def inc(inst, a, b, pc):
    if inst[1] == 'a':
        a += 1
    elif inst[1] == 'b':
        b += 1

    return a, b, pc + 1

def jmp(inst, a, b, pc):
    return a, b, pc + inst[1]

def jie(inst, a, b, pc):
    val = a if inst[1] == 'a' else b
    pc += inst[2] if val % 2 == 0 else 1

    return a, b, pc

def jio(inst, a, b, pc):
    val = a if inst[1] == 'a' else b
    pc += inst[2] if val == 1 else 1

    return a, b, pc

def execute_program(instructions, initial_a = 0):
    a, b, pc = initial_a, 0, 0
    while pc in range(0, len(instructions)):
        inst = instructions[pc]

        if inst[0] == 'hlf':
            a, b, pc = hlf(inst, a, b, pc)

        elif inst[0] == 'tpl':
            a, b, pc = tpl(inst, a, b, pc)

        elif inst[0] == 'inc':
            a, b, pc = inc(inst, a, b, pc)

        elif inst[0] == 'jmp':
            a, b, pc = jmp(inst, a, b, pc)

        elif inst[0] == 'jio':
            a, b, pc = jio(inst, a, b, pc)

        elif inst[0] == 'jie':
            a, b, pc = jie(inst, a, b, pc)

    return b

if __name__ == '__main__':
    
    instructions = []
    f = open('data')
    for line in f:
        instructions.append(parse(line))

    f.close()

    print('[Part 1] Value of "b" is', execute_program(instructions))
    print('[Part 2] Value of "b" is', execute_program(instructions, initial_a = 1))
