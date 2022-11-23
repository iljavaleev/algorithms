"""
Given a string s, return the longest palindromic substring in s.

Example 1:
Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.

Example 2:
Input: s = "cbbd"
Output: "bb"
"""


def find_variants(i):
    return ((a, b) for a in range(i)
            for b in range(-i + 1, 1) if abs(a) + abs(b) == i)


def find_palindromic(s):
    s = list(s)
    n = len(s)
    for i in range(n):
        ss1 = s[i:]
        ss2 = s[:n - i]
        if ss1 == ss1[::-1]:
            return ''.join(ss1)
        if ss2 == ss2[::-1]:
            return ''.join(ss2)
        extra = find_variants(i)
        for l, r in extra:
            ss = s[l:r]
            if ss == ss[::-1]:
                return ''.join(ss)


def find_palindromic1(s):
    string = list(s)
    reversed_string = string[::-1]
    n = len(s)
    max_count = 0
    count = 0
    for i in range(n):
        if string[i] == reversed_string[i]:
            count += 1
        else:
            if count > max_count:
                max_count = count
            count = 0
    return max_count


def find_palindromic1(s):
    string = list(s)
    n = len(s)
    max_count = 0
    start = 0
    count = 0
    for i in range(n):
        if string[i] == string[-i - 1]:
            start = i
            count += 1
        else:
            if count > max_count:
                max_count = count

            count = 0
    return max_count



# s = "babad"
# n = len(s)
# print(s[:-1])
# print(s[::-1])
# print(find_palindromic(s))
# print(find_variants(2))
# i = 2
# print(list(range(i)))
# print(list(range(-i + 1, 1)))
import builtins
from typing import Type

def check_int(a=None):
    wrong = "Введенное число {} неправильного типа"
    match a:
        case None:
            i = input()
            match i:
                case str() if i.isdigit():
                    return True
                case _:
                    return wrong.format(i)
        case int():
            return True
        case _:
            return wrong.format(a)

assert check_int(4) == True
assert check_int(4.02) == "Введенное число 4.02 неправильного типа"