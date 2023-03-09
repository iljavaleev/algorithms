class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None


class LinkedListDequeue:

    def __init__(self):
        self._left = None
        self._right = None
        self._size = 0


    def push_back(self, value):
        node = Node(value)

        if self._right is None:
            self._left = node
            self._right = node
        else:
            node.prev = self._right
            self._right.next = node
            self._right = node
        self._size += 1


    def push_front(self, value):
        node = Node(value)

        if self._left is None:
            self._left = node
            self._right = node
        else:
            node.next = self._left
            self._left.prev = node
            self._left = node
        self._size += 1

    def peek_front(self):
        if self._left is None:
            return "error"
        return self._left.value

    def peek_back(self):
        if self._right is None:
            return "error"
        return self._right.value

    def pop_front(self):
        if self._left is None:
            return "error"

        tmp = self._left
        val = tmp.value

        self._left = tmp.next

        if self._left is not None:
            self._left.prev = None
        else:
            self._right = None

        tmp = None

        self._size -= 1
        return val

    def pop_back(self):
        if self._right is None:
            return "error"

        tmp = self._right
        val = tmp.value

        self._right = tmp.prev
        if self._right is not None:
            self._right.next = None
        else:
            self._left = None

        tmp = None

        self._size -= 1
        return val

    def clear(self):
        while self._left is not None:
            tmp = self._left
            self._left = self._left.next
            tmp = None
        self._size = 0
        self._left = None
        self._right = None

    def __len__(self):
        return self._size


if __name__ == '__main__':
    deq = LinkedListDequeue()
    lines = []
    with open('input.txt') as f:
        for line in f:
            lines.append(line.split())
    for l in lines:
        if l[0] == 'push_front':
            deq.push_front(l[1])
            print('ok')
        elif l[0] == 'push_back':
            deq.push_back(l[1])
            print('ok')
        else:
            if l[0] == 'pop_front':
                print(deq.pop_front())
            elif l[0] == 'pop_back':
                print(deq.pop_back())
            elif l[0] == 'front':
                print(deq.peek_front())
            elif l[0] == 'back':
                print(deq.peek_back())
            elif l[0] == 'size':
                print(len(deq))
            elif l[0] == 'clear':
                deq.clear()
                print('ok')
            elif l[0] == 'exit':
                print('bye')
                break