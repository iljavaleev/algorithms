def polish(l):
    stack = []
    for i in l:
        if i.isdigit():
            stack.append(int(i))
        else:
            if len(stack) >= 2:
                second, first = stack.pop(), stack.pop()
                if i == '*':
                    stack.append(first * second)
                elif i == '-':
                    stack.append(first - second)
                else:
                    stack.append(first + second)
    return stack[0]

if __name__ == '__main__':
    s = input().split()
    print(polish(s))
