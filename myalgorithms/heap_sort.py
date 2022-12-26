import heapq


def heap_sort(A):
    H = []
    for element in A:
        heapq.heappush(H, element)

    # heapq.heapify(A)
    # H = A
    return [heapq.heappop(H) for _ in range(len(H))]


if __name__ == "__main__":
    l = [1, 3, 2, -100, 4, 66, -44, 0]
    print(heap_sort(l))