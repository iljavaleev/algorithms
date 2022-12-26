from functools import reduce
from operator import mul

def get_prime_numbers(n):
    r = []
    for i in range(2, n):
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            r.append(i)
    return r


def calc_prime_factors(value):
    primes = get_prime_numbers(value)
    value_copy = value
    d = []
    for i in primes:
        if value_copy == 1:
            return d
        while True:
            if value_copy % i == 0:
                value_copy //= i
                d.append(i)
                continue
            else:
                break

# value = 1111
# result = calc_prime_factors(value)
# assert value == reduce(mul, result)
print(get_prime_numbers(15))