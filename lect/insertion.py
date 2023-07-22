def isort(l):
    for i in range(1, len(l)):
        key = l[i]
        j = i - 1
        while j > -1 and l[j] > key:
            l[j + 1] = l[j]
            j -= 1
        l[j + 1] = key


def rec_isort(l, last):
    if last <= 1:
        return

    rec_isort(l, last - 1) # n-1 вызов рекурсии

    key = l[last]   # время для вставки элемент, которое зависит от n - 1
    j = last - 1
    while j > -1 and l[j] > key:
        l[j + 1] = l[j]
        j -= 1
    l[j + 1] = key


if __name__ == '__main__':
    l = [5, 2, 4, 6, 1, 3]
    # isort(l)
    # print(l)

    rec_isort(l, len(l) - 1)
    print(l)
