def combinations(iterable, r):
    # combinations('ABCD', 2) --> AB AC AD BC BD CD
    # combinations(range(4), 3) --> 012 013 023 123
    pool = tuple(iterable) # перевод в tuple
    n = len(pool) # длина tuple
    if r > n: # if length of combination is greater than length of the tuple
        return
    indices = list(range(r)) # list of indices by comb len
    a = tuple(pool[i] for i in indices)
    yield tuple(pool[i] for i in indices)
    while True:
        for i in reversed(range(r)):
            if indices[i] != i + n - r:
                break
        else:
            return
        indices[i] += 1
        for j in range(i+1, r):
            indices[j] = indices[j-1] + 1
        yield tuple(pool[i] for i in indices)


a = combinations('ABCD', 2)
print(a.__next__())
