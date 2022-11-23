"""
Two numbers n1 and n2 are called friends (or related) if the sum of their divisors is equal
to the other number:
        sum(divisors(n1)) = n2
        sum(divisors(n2)) = n1
Write function calc_friends(max_exclusive) to compute all friends numbers up to
a passed maximum value.
"""
from array import array


def get_divisors(n):
    divisors = array('i', [])
    for i in range(1, n):
        if n % i == 0:
            divisors.append(i)
    return divisors


def calc_friends(max_exclusive):
    return [(a, b) for a in range(1, max_exclusive)
            for b in range(1, a + 1) if a == sum(get_divisors(b))
            and b == sum(get_divisors(a))]


if __name__ == '__main__':
    print(calc_friends(300))
