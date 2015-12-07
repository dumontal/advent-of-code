#!/usr/bin/env python

def north(p):
	return (p[0], p[1] + 1)

def south(p):
	return (p[0], p[1] - 1)

def east(p):
	return (p[0] + 1, p[1])

def west(p):
	return (p[0] - 1, p[1])

def next_position(p, m):
	if m == '^':
		return north(p)
	elif m == 'v':
		return south(p)
	elif m == '<':
		return west(p)
	elif m == '>':
		return east(p)

pos_santa = (0, 0)
pos_robo_santa = (0, 0)
visited = {(0, 0)}

# Binary variable to show whose turn it is.
# Santa begins first.
turn = 0

f = open('data')
for move in f.read():
	if turn == 0:
		pos_santa = next_position(pos_santa, move)
		visited.add(pos_santa)
	else:
		pos_robo_santa = next_position(pos_robo_santa, move)
		visited.add(pos_robo_santa)

	turn = (turn + 1) % 2

f.close()
print(len(visited), 'houses have had at least one present.')
