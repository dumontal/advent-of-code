#!/usr/bin/env python

def say(letter, count):
    if count > 3:
        # Count should never be more than 3.
        print('Found count =', count, '. Something might be wrong.')

    return str(count) + letter

def play(word):
    result = ''

    last_letter = None
    count = 0
    for letter in word:
        if last_letter is not None:
            if letter != last_letter:
                result += say(last_letter, count)
                count = 0

        last_letter = letter
        count += 1

    if last_letter is not None:
        result += say(last_letter, count)

    return result

puzzle = '1113222113'

for i in range(40):
    puzzle = play(puzzle)

print('Length of resulting puzzle after 40 times is:', len(puzzle))

for i in range(10):
    puzzle = play(puzzle)

print('Length of resulting puzzle after 50 times is:', len(puzzle))

# print(play('1'))
# print(play('11'))
# print(play('21'))
# print(play('1211'))
# print(play('111221'))
