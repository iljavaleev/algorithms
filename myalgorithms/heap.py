from random import shuffle


class Heap:
    def __init__(self, iter=None):
        if iter is not None:
            self.heap = list(iter)
        else:
            self.heap = list()

    def swap(self, fr, to):
        self.heap[fr], self.heap[to] = self.heap[to], self.heap[fr]

    def bubble_up(self, i):
        while i > 0 and self.heap[i] < self.heap[(i - 1)//2]:
            self.swap(i, (i - 1) // 2)
            i = (i - 1) // 2

    def bubble_down(self, i):
        left = 2 * i + 1
        right = 2 * i + 2
        while (2 * i) + 1 <= len(self.heap) \
                and (self.heap[i] > self.heap[left]
                     or self.heap[i] > self.heap[right]):
            if self.heap[left] > self.heap[right]:
                self.swap(i, right)
                i = right
            else:
                self.swap(i, left)
                i = left
            left = 2 * i + 1
            right = 2 * i + 2

    def insert(self, obj):
        self.heap.append(obj)
        self.bubble_up(len(self.heap) - 1)

    def extract_min(self):
        minimum = self.heap[0]
        self.heap[0] = self.heap.pop()
        self.bubble_down(0)
        return minimum

    def find_min(self):
        return self.heap[0]

    def delete(self, i):
        self.heap[i] = self.heap.pop()
        if self.heap[i] > self.heap[(i - 1)//2]:
            self.bubble_up(i)
        elif self.heap[i] < self.heap[(i - 1)//2]:
            self.bubble_down(i)

    def __str__(self):
        return ' '.join((str(i) for i in self.heap))


if __name__ == '__main__':
    l = [4, 4, 8, 9, 4, 12, 9, 11, 13, 7, 10, 0, 99]
    h = Heap(l)
    h.insert(5)
    h.insert(1)
    shuffle(l)

    h = Heap(l)
    print(l)
    print(h)
    a = h.extract_min()
    print(a)
    print(h)
    h.delete(4)
    print(h)


