class MyQueue:

    def __init__(self, capacity=100):
        self.capacity = capacity
        self._array = [None] * capacity
        self._head = 0
        self._tail = 0
        self._size = 0

    def is_empty(self):
        return self._size == 0

    def enqueue(self, value):
        if self._tail == len(self._array):
            self._expand()
        self._array[self._tail] = value
        self._tail += 1
        self._size += 1

    def dequeue(self):
        if self.is_empty():
            return 'error'
        value = self._array[self._head]
        self._array[self._head] = None
        self._head += 1
        self._size -= 1
        return value

    def peek(self):
        if self.is_empty():
            return 'error'
        return self._array[self._head]

    def _expand(self):
        self._array += [None] * len(self._array)

    def clear(self):
        self._array.clear()
        self._array += [None] * self.capacity
        self._head = 0
        self._tail = 0
        self._size = 0

    def __len__(self):
        return self._size


if __name__ == '__main__':
    ar_queue = MyQueue()
    lines = []
    with open('input.txt') as f:
        for line in f:
            lines.append(line.split())
    for l in lines:
        if l[0] == 'push':
            ar_queue.enqueue(l[1])
            print('ok')
        else:
            if l[0] == 'pop':
                print(ar_queue.dequeue())
            elif l[0] == 'front':
                print(ar_queue.peek())
            elif l[0] == 'size':
                print(len(ar_queue))
            elif l[0] == 'clear':
                ar_queue.clear()
                print('ok')
            elif l[0] == 'exit':
                print('bye')
                break
