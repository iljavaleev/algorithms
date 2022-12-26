import heapq


def heap_median(A):
    H_1 = [A[0] * (-1)]
    H_2 = [A[1]]

    for i in range(2, len(A)):
        if H_1[0] * (-1) > A[i]:
            heapq.heappush(H_1, A[i] * (-1))
        else:
            heapq.heappush(H_2, A[i])

        if len(H_1) >= len(H_2) + 2:
            heapq.heappush(H_2, heapq.heappop(H_1) * (-1))
        if len(H_2) >= len(H_1) + 2:
            heapq.heappush(H_1, heapq.heappop(H_2) * (-1))

    if len(A) % 2:
        return H_2[0]
    else:
        return H_1[0] * (-1), H_2[0]


if __name__ == "__main__":
    l = [-100, -44, 0, 1, 2, 3, 4, 66, 12, 99]
    print(heap_median(l))
    print(sorted(l))