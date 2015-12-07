#!/usr/bin/env python

import re

def decoded_length(line):
	# Note: we're only interested in the string length
	# so we can replace our expressions by a sigle char 'A'
	interpreted_line = line[1 : len(line) - 1]
	interpreted_line = re.sub(r'\\\\',    'A', interpreted_line)
	interpreted_line = re.sub(r'\\\"',    'A', interpreted_line)
	interpreted_line = re.sub(r'\\x\w\w', 'A', interpreted_line)
	return len(interpreted_line)

def encoded_length(line):
	# Note: we're only interested in the string length
	# so we can replace our expressions by a sigle char 'A'
	n_line = line[1 : len(line) - 1]
	n_line = re.sub(r'\\\\', 'AAAA', n_line)
	n_line = re.sub(r'\\\"', 'AAAA', n_line)
	n_line = re.sub(r'\\x', 'AAx', n_line)
	return len(n_line) + 6

difference_decoded = 0
difference_encoded = 0
f = open('data')
for l in f:
	line = l.replace('\n', '')

	difference_decoded += len(line) - decoded_length(line)
	difference_encoded += encoded_length(line) - len(line)

f.close()

print('Part 1 expected value is:', difference_decoded)
print('Part 2 expected value is:', difference_encoded)
