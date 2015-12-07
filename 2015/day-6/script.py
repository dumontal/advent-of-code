#!/usr/bin/env python

import re
import sys

def parse_line(line, pattern):
	match = pattern.match(line)
	if match is None:
		print('Line "', line, '" does not match. Aborting.')
		sys.exit(1)

	action = match.group(1)
	xs = int(match.group(2))
	ys = int(match.group(3))
	xe = int(match.group(4))
	ye = int(match.group(5))
	return ( action, xs, xe, ys, ye )

# At init time, there is no lights at all.
grid = [[ 0 for i in range(0, 1000) ] for j in range(0, 1000)]

pattern = re.compile('.*(turn off|toggle|turn on)\s*(\d+),(\d+)\s*through\s*(\d+),(\d+).*')

f = open('data')
for line in f:
	action, xs, xe, ys, ye = parse_line(line, pattern)

	for i in range(xs, xe + 1):
		for j in range(ys, ye + 1):

			if action == 'turn on':
				grid[i][j] += 1

			elif action == 'turn off':
				grid[i][j] = max(0, grid[i][j] - 1)

			elif action == 'toggle':
				grid[i][j] += 2

f.close()
print(sum([sum(row) for row in grid]))
