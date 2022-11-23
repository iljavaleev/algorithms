"""
Suppose you have a collection of coins or numbers of different values. Write function
calc_max_possible_change(values) that determines, for positive integers, what
amounts can be seamlessly generated with it starting from the value 1. The maximum
value should be returned as a result.
"""

import itertools


def calc_max_possible_change(values):
    result = {1}
    cash = set()
    prev = 1
    for L in range(1, len(values) + 1):
        for subset in itertools.combinations(values, L):
            add = sum(subset)
            if prev + 1 in cash:
                result.add(prev + 1)
                cash.remove(prev + 1)
                prev += 1
            if add not in result and prev + 1 == add:
                result.add(add)
                prev = add
                continue
            cash.add(add)
    return result, prev

print(calc_max_possible_change([1, 1, 1, 1, 5, 10, 20, 50]))