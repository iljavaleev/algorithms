# print(''.join((str(x) for x in range(124))).replace('9', ''), end='')

# def is_odd(a):
#     return a % 2
#
# for i in range(0, 100, 10):
#     if is_odd(i // 10):
#         print(*range(i + 10, i, -1))
#     else:
#         print(*range(i + 1, i + 11))

# for i in range(32, 127):
#     print(chr(i), end='')
#
# l = list('asdfgh')
#
#
# def print_index(l, fr=None, to=None):
#     if not fr:
#         fr = 1
#     if not to:
#         to = len(l)
#     if to:
#         to += 1
#     for i in range(fr, to):
#         print(f'элемент {l[i-1]} находится в списке под индексом {i}')
#
# # print_index(l, fr=4)
#
#
# my_list = [[1, 2, 3], [40, 50, 60], [9, 8, 7]]
# import functools
# print(functools.reduce(lambda a, b: a+b, [sub[1] for sub in my_list]))
#
# import operator
# functools.reduce(operator.add, [sub[1] for sub in my_list], 0)
#
# def get_creators(record: dict) -> list:
#     match record:
#         case {'type': 'book', 'api': 2, 'authors': [*names]}: # сравнение по 'type': 'book', 'api': 2 и 'authors' должен иметь значение последовательности. Возвращается список
#             return names
#         case {'type': 'book', 'api': 1, 'author': name}:# сравнение по 'type': 'book', 'api': 2 и 'authors' может быть любым объектом. Возвращается список
#             return [name]
#         case {'type': 'book'}:
#             raise ValueError(f"Invalid 'book' record: {record!r}")
#         case {'type': 'movie', 'director': name}:
#             return [name]
#         case _:
#             raise ValueError(f'Invalid record: {record!r}')
#
# # b1 = dict(api=1, author='Douglas Hofstadter', type='book', title='Gödel, Escher, Bach')
# b1 = {'api': 1, 'author': 'Douglas Hofstadter', 'type': 'book', 'title':'Gödel, Escher, Bach'}
# print(get_creators(b1))
# b2 = dict(api=2, type='book', title='Python in a Nutshell', authors='Martelli Ravenscroft Holden'.split())
# print(get_creators(b2))
# print(get_creators({'type': 'book', 'pages': 770}))

# def circular():
#     while True:
#         for connection in ['a', 'b', 'c']:
#             yield connection

# from itertools import cycle
#
# lst = ['a', 'b', 'c']
#
# pool = cycle(lst)
#
# for _ in range(20):
#     print(next(pool))

# from random import randint as r
# l = 10 * [None]
#
# n = len(l)
# h1 = r(0, n)
# h2 = r(0, n)
# check = 0
# it = 0
#
# while check != n:
#     if l[h1] is None:
#         l[h1] = 1
#         check += 1
#     else:
#         h2 = r(0, n)
#         h1 = (h1 + h2) % n
#     print(l)
#     it += 1
# print(it, l)
w = 'asdf'
l = []
for i in range(len(w)):
    l.append(w[:i] + w[i+1:])
print(l)