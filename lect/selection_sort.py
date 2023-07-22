def selection_sort(A, n):
    for i in range(n-1):
        mini = i
        for j in range(i+1, n):
            if A[j] < A[mini]:
                mini = j
        A[i], A[mini] = A[mini], A[i]


if __name__ == '__main__':
    l = [1, 34, -99, 0, 12, 12, 34, 200]
    selection_sort(l, len(l))
    print(l)