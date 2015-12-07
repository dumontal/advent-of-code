#!/usr/bin/env python

import hashlib

def is_advent_coin(secret, key):
	secret = secret + str(key)
	digest = hashlib.md5(secret.encode('utf-8')).hexdigest()
	return digest.startswith('000000')

key = 0
secret = 'bgvyzdsv'
while not is_advent_coin(secret, key):
	if (key % 10000) == 0:
		print('Processed 10000 keys so far...')

	key += 1

print(key)
