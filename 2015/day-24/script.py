#!/usr/bin/env python

from itertools import combinations
from functools import reduce
import operator

def next_combination(elems, target_weight):
    return (cb for i in range(1, len(elems)) for cb in combinations(elems, i) if sum(cb) == target_weight)

def diff(elems, to_subtract):
    return list(set(elems) - set(to_subtract))

def partition_exists(weights, target_weight, n_groups):
    for combination in next_combination(weights, target_weight):
        if n_groups > 2:
            return partition_exists(diff(weights, combination), target_weight, n_groups - 1)

        # This combination holds and there is two of them to find => it's ok.
        return True

    return False

def partition(weights, n):  
    target_weight = sum(weights) // n
    res = set()
    size = len(weights)

    for combination in next_combination(weights, target_weight):
        if partition_exists(diff(weights, combination), target_weight, n - 1):
            if len(combination) > size:
                return res
            
            res.add(combination)
            size = len(combination)

def min_quantum_entanglement(combinations):
    return min(map(lambda c: reduce(operator.mul, c), combinations))

if __name__ == '__main__':
    
    weights = []
    with open('data') as f:
        weights = [int(l) for l in f]

    qe = min_quantum_entanglement(partition(weights, 3))
    print('[Part 1] Minimum quantum entanglement is', qe)

    qe = min_quantum_entanglement(partition(weights, 4))
    print('[Part 2] Minimum quantum entanglement is', qe)
