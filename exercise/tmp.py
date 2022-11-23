# print(''.join((str(x) for x in range(124))).replace('9', ''), end='')

# def is_odd(a):
#     return a % 2
#
# for i in range(0, 100, 10):
#     if is_odd(i // 10):
#         print(*range(i + 10, i, -1))
#     else:
#         print(*range(i + 1, i + 11))
#
# for i in range(32, 127):
#     print(chr(i), end='')

l = list('asdfgh')


def print_index(l, fr=None, to=None):
    if not fr:
        fr = 1
    if not to:
        to = len(l)
    if to:
        to += 1
    for i in range(fr, to):
        print(f'элемент {l[i-1]} находится в списке под индексом {i}')

print_index(l, fr=4)
