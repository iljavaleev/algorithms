from array import array


def value_count(values):
    max = (0, 0)
    for i in set(values):
        c = values.count(i)
        if c > max[1]:
            max = i, c

    return max


def merge(v1, v2):
    if not v1:
        return v2
    if not v2:
        return v1

    for i in range(len(v1)):
        if v1[i] >= v2[0]:
            v1.insert(i, v2.pop(0))
    if v2:
        v1+=v2
    return v1


print(merge([2, 3, 5, 7, 11], [7, 11, 13, 17]))


def addition(l1, l2):
    r = 0
    l = array('i', [])
    for i in range(len(l1) - 1, -1, -1):
        s = l1[i] + l2[i]
        d = s % 10
        if r:
            d += 1
            r = 0
        r += s//10
        l.insert(0, d)
    if r:
        l.insert(0, r)
    return l

print(addition([9, 2, 7], [1, 3, 5]))
print(addition([1, 2, 3], [4, 5, 6]))
print(addition([9, 9, 9], [9, 9, 9]))