'''
Полиномиальный хеш
Алле очень понравился алгоритм вычисления полиномиального хеша.
Помогите ей написать функцию, вычисляющую хеш строки s.
В данной задаче необходимо использовать в качестве значений отдельных символов их коды в таблице ASCII.
'''
from operator import add
from functools import reduce
# s = 'hash'
# a = 123
# m = 100003
# r = 0
# n = len(s)

a = 1000
m = 123987123

def get_hash(s, a, m):
    n = len(s)
    return reduce(add, (ord(s[i]) * a**(n - i - 1) for i in range(n))) % m

from random import shuffle

l = list(range(97, 123))
def get_hash(s, a, m):
    n = len(s)
    return reduce(add, (s[i] * a**(n - i - 1) for i in range(n))) % m

n = 0
r = []
i = 0
while True:
    shuffle(l)
    s1 = l.copy()[: 2**i]
    shuffle(l)
    s2 = l.copy()[: 2**i]
    if get_hash(s1, a, m) == get_hash(s2, a, m):
        r.append(s1)
        r.append(s2)
        break
    i += 1
print(r)
# for i in r:
#     ''.join([chr(j) for j in i])

# s1 = 'ezhgeljkablzwnvuwqvp'
# s2 = 'gbpdcvkumyfxillgnqrv'
# s1 = 'AAa'
# s2 = 'BbB'
# print(get_hash(s1, a, m))
# print(get_hash(s2, a, m))


# for i in s1:
#     print(ord(i), end=' ')
# print()
# for i in s2:
#     print(ord(i), end=' ')
#
# print()
# for i, j in zip(s1, s2):
#     print(ord(i) - ord(j), end=' ')




