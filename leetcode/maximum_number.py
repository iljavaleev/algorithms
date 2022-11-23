"""
You are given a positive integer num consisting only of digits 6 and 9.

Return the maximum number you can get by changing at most one digit (6 becomes 9, and 9 becomes 6).

Input: num = 9669
Output: 9969

Input: num = 9996
Output: 9999
"""

def get_max(num):
    l = list(str(num))
    n = len(l)
    for i in range(n):
        if l[i] == '6':
            l[i] = '9'
            break
    return int(''.join(l))

print(get_max(9999))