def heapify(heap, n, i):
    left = 2 * i + 1
    right = 2 * i + 2

    while 2 * i < n:
        if left < n and heap[left] > heap[i]:
            min_el_idx = i
        else:
            min_el_idx = left
        if right < n and heap[min_el_idx] > heap[right]:
            min_el_idx = right
        if i != min_el_idx:
            heap[i], heap[min_el_idx] = heap[min_el_idx], heap[i]
        else:
            break


def print_sorted(heap):

    start_idx = len(heap) // 2
    for i in range(start_idx - 1, -1, -1):
        heapify(heap, len(heap), i)

    for i in range(len(heap) - 1, -1, -1):
        heap[0], heap[i] = heap[i], heap[0]
        print(heap[0], end=' ')
        heapify(heap, i, 0)




if __name__ == '__main__':
    _ = input()
    heap = [int(x) for x in input().split()]
    print_sorted(heap)


