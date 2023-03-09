from collections import OrderedDict, Counter


def find_an(l):
    d = OrderedDict()

    for i in range(len(l)):
        d.setdefault(frozenset(Counter(l[i])), []).append(i)

    for i in d.values():
        print(*i)

def find_an2(l):
    d = OrderedDict()

    for i in range(len(l)):
        d.setdefault(str(sorted(l[i])), []).append(i)

    for i in d.values():
        print(*i)



if __name__ == '__main__':
    _ = input()
    l = input().split()
    find_an2(l)

