#!/usr/bin/env python

def parse_dims(line):
	dims = [ int(x) for x in line.replace('\n', '').split('x') ]
	dims.sort()
	return (dims[0], dims[1], dims[2])

def compute_area(i, j, k):
	return (3 * i * j) + (2 * i * k) + (2 * j * k)

def compute_ribbon_area(i, j, k):
	return i * j * k + 2 * i + 2 * j

paper_area = 0
ribbon_area = 0
f = open('data')
for line in f:
	i, j, k = parse_dims(line)
	paper_area += compute_area(i, j, k)
	ribbon_area += compute_ribbon_area(i, j, k)

f.close()
print('Paper area is:', paper_area)
print('Ribbon area is:', ribbon_area)
