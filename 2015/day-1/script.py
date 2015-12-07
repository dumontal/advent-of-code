#!/usr/bin/env python

floor = 0
update_basement = True
basement = 0

f = open('data')
for c in f.read():
	if update_basement:
		basement += 1

	if c == '(':
		floor += 1
	elif c == ')':
		floor -= 1

	if floor == -1:
		update_basement = False

f.close()
print('Last floor is:', floor)
if not update_basement:
	print('Basement reached at', basement)
