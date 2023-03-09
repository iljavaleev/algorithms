# maxheap
class Heap:

    def __init__(self, iter=None):
        self.current_size = 0
        if iter is not None:
            self.heap = list(iter)
        else:
            self.heap = list()

    def _bubble_up(self, i):
        while i > 0 and self.heap[i] > self.heap[(i - 1) // 2]:
            self.heap[i], self.heap[(i-1)//2] = self.heap[(i-1)//2], self.heap[i]
            i = (i - 1) // 2

    def insert(self, val):
        self.heap.append(val)
        self._bubble_up(len(self.heap) - 1)

    def _max_child(self, i):
        current_size = len(self.heap) - 1
        if 2 * i + 1 > current_size:
            return i
        if 2 * i + 2 > current_size:
            return 2 * i + 1
        if self.heap[2 * i + 1] > self.heap[2 * i + 2]:
            return 2 * i + 1
        else:
            return 2 * i + 2

    def pop_head(self):
        max = self.heap[0]
        self.heap[0] = self.heap[-1]
        i = 0
        while i * 2 + 2 < len(self.heap):
            max_son_idx = self._max_child(i)
            if self.heap[i] < self.heap[max_son_idx]:
                self.heap[max_son_idx], self.heap[i] \
                    = self.heap[i], self.heap[max_son_idx]
                i = max_son_idx
            else:
                break
        self.heap.pop()
        return max

    def print_sorted(self):
        while self.heap:
            print(self.pop_head(), end=' ')


if __name__ == '__main__':
    heap = Heap()
    _ = input()
    for i in [int(x) for x in input().split()]:
        heap.insert(i)
    heap.print_sorted()

