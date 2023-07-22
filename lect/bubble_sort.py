def bubblesort(A, n):
    for i in range(n - 1):
        for j in range(n - 1, i, -1):
            if A[j] < A[j - 1]:
                A[j], A[j - 1] = A[j - 1], A[j]


if __name__ == '__main__':
    l = [12, 2, 100, -100, 99, 23, 33]
    bubblesort(l, len(l))
    print(l)
