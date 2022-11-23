"""
This exercise deals with three-digit Armstrong numbers. By definition, these are
numbers for whose digits x, y, and z from 1 to 9 satisfy the following equation:
    x * 100 + y * 10 + z = x^3 + y^3 + z^3
Write function calc_armstrong_numbers() to compute all Armstrong numbers for x,
y, and z (each < 10).
"""

def find_armstrong_numbers(a, b, c):
    return [(x, y, z) for x in range(10) for y in range(10) for z in range(10)
            if x * 100 + y * 10 + z == x**a + y**b + z**c]


print(*find_armstrong_numbers(3, 3, 3), sep='\n')
print('---------')
print(*find_armstrong_numbers(1, 2, 3), sep='\n')
print('---------')
print(*find_armstrong_numbers(3, 2, 1), sep='\n')