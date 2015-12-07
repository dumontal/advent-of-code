#!/usr/bin/env python

import re

def is_nice(line):
	vowels    = { 'a', 'e', 'i', 'o', 'u' }
	forbidden = { 'ab', 'cd', 'pq', 'xy' }

	number_of_vowels = 0
	has_double = False

	old = None
	for c in line:
		if c in vowels:
			number_of_vowels += 1

		if old is not None:
			if (old + c) in forbidden:
				return False

			if not has_double and old is c:
				has_double = True

		old = c

	return number_of_vowels >= 3 and has_double

def satisfies_rule_1_v2(line):
	for i in range(len(line) - 1):
		word = line[i] + line[i + 1]
		pos = [ m.start() for m in re.finditer(word, line) ]

		if len(pos) >= 2:
			return True

	return False

def satisfies_rule_2_v2(line):
	for c in line:
		pos = [ m.start() for m in re.finditer(c, line) ]
		for i in range(len(pos) - 1):

			if (pos[i + 1] - pos[i]) == 2:
				# There is only one letter between two occurrences of 'c'.
				return True

	return False

def is_nice_v2(line):
	return satisfies_rule_1_v2(line) and satisfies_rule_2_v2(line)

f = open('data')
count = 0
for l in f:
	if is_nice_v2(l.replace('\n', '')):
		count += 1

f.close()
print(count)

# print('ugknbfddgicrmopn', is_nice('ugknbfddgicrmopn'))
# print('aaa', is_nice('aaa'))
# print('jchzalrnumimnmhp', is_nice('jchzalrnumimnmhp'))
# print('haegwjzuvuyypxyu', is_nice('haegwjzuvuyypxyu'))
# print('dvszwmarrgswjxmb', is_nice('dvszwmarrgswjxmb'))

# print('qjhvhtzxzqqjkmpb', is_nice_v2('qjhvhtzxzqqjkmpb'))
# print('xxyxx', is_nice_v2('xxyxx'))
# print('uurcxstgmygtbstg', is_nice_v2('uurcxstgmygtbstg'))
# print('ieodomkazucvgmuy', is_nice_v2('ieodomkazucvgmuy'))