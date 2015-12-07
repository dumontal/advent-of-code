#!/usr/bin/env python

import re

def decode_binary(line):
	match = re.match(r'\s*(\w+)\s*(AND|OR|LSHIFT|RSHIFT)\s*(\w+)\s*->\s*(\w+).*', line)

	lfs = match.group(1)
	if lfs.isdigit():
		lfs = int(lfs)

	rhs = match.group(3)
	if rhs.isdigit():
		rhs = int(rhs)

	return (match.group(4), match.group(2), lfs, rhs)

def decode_unary(line):
	match = re.match(r'\s*(NOT)?\s*(\w+)\s*->\s*(\w+).*', line)
	
	arg = match.group(2)
	if arg.isdigit():
		arg = int(arg)

	return (match.group(3), match.group(1), arg)

def decode_action(line):
	match = re.match(r'.*(LSHIFT|RSHIFT|AND|OR).*', line)
	
	if match is None:
		return decode_unary(line)
	else:
		return decode_binary(line)

def is_computed(signal, all_wires):
	return ( type(signal) is int ) or ( all_wires[signal] is not None )

def can_compute_signal(action, all_wires):
	op = action[1]
	if op == 'NOT' or op is None: # Unary case
		return is_computed(action[2], all_wires)
	else: # Binary case
		return is_computed(action[2], all_wires) and is_computed(action[3], all_wires)

	return False

def compute_signal(action, all_wires):
	op = action[1]
	signal = None

	if ( op is None ) and ( type(action[2]) is int ):
		signal = action[2]
	elif op is None: # Assign signal to another one
		signal = all_wires[action[2]]
	elif op == 'NOT':
		signal = ~ all_wires[action[2]]
	elif op == 'LSHIFT':
		signal = all_wires[action[2]] << action[3]
	elif op == 'RSHIFT':
		signal = all_wires[action[2]] >> action[3]
	elif op == 'AND':
		in1 = action[2] if ( type(action[2]) is int ) else all_wires[action[2]]
		in2 = action[3] if ( type(action[3]) is int ) else all_wires[action[3]]
		signal = in1 & in2
	elif op == 'OR':
		in1 = action[2] if ( type(action[2]) is int ) else all_wires[action[2]]
		in2 = action[3] if ( type(action[3]) is int ) else all_wires[action[3]]
		signal = in1 | in2

	# normalize signal to 16 bits
	signal = signal % (2 ** 16)
	all_wires.update({ action[0] : signal })

wires = dict()
actions_remaining = set()

f = open('data')
for line in f:
	data = decode_action(line)
	wires.update( { data[0] : None } )
	actions_remaining.add( data )

f.close()

print('Applying all actions on the wires...')

while len(actions_remaining) > 0:
	actions_performed = set()

	for action in actions_remaining:
		if can_compute_signal(action, wires):
			compute_signal(action, wires)
			actions_performed.add(action)

	# Difference between two sets.
	actions_remaining = actions_remaining - actions_performed

print('Signal ultimately provided to a is:', wires['a'])
