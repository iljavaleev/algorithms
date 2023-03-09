class Stack:
    def __init__(self):
        self._array = list()

    def is_empty(self):
        return not bool(self._array)

    def push(self, value):
        self._array.append(value)

    def pop(self):
        if self.is_empty():
            return 'error'
        return self._array.pop()

    def peek(self):
        if self.is_empty():
            return 'error'
        return self._array[-1]

    def clear(self):
        self._array.clear()

    def size(self):
        return len(self._array)


if __name__ == '__main__':
    stack = Stack()
    lines = []
    with open('input.txt') as f:
        for line in f:
            lines.append(line.split())
    for l in lines:
        if l[0] == 'push':
            stack.push(l[1])
            print('ok')
        else:
            if l[0] == 'pop':
                print(stack.pop())
            elif l[0] == 'back':
                print(stack.peek())
            elif l[0] == 'size':
                print(stack.size())
            elif l[0] == 'clear':
                stack.clear()
                print('ok')
            elif l[0] == 'exit':
                print('bye')
                break

