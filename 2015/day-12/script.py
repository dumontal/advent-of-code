#!/usr/bin/env python

import json

def parse_list(arr):
    return sum(list(map(parse_object, arr)))

def parse_object(obj):
    if type(obj) is int:
        return obj

    elif type(obj) is list:
        return parse_list(obj)

    elif type(obj) is dict:
        if PART_TWO and ('red' in obj.values()):
            return 0

        return parse_list(obj.values())

    # Do not know how to decode, type(obj), obj
    # It must be a colour name.
    return 0

f = open('data')
content = f.read()
f.close()

data = json.loads(content)

PART_TWO = False
print('Sum is (part one)', parse_object(data))

PART_TWO = True
print('Sum is (part two)', parse_object(data))
