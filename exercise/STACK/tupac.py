def tupac(l, N):
    rev = l[::-1]
    stack = []
    prev = None
    new = []
    i = 0
    while True:
        get = rev.pop()
        if get == 1:
            new.append(get)
            prev = 1
            i += 1
            break
        stack.append(get)
    while i < N:
        if stack and stack[-1] == prev + 1:
            get = stack.pop()
            new.append(get)
            prev = get
            i += 1
            continue
        elif rev and rev[-1] == prev + 1:
            get = rev.pop()
            new.append(get)
            prev = get
            i += 1
            continue
        elif rev:
            stack.append(rev.pop())
        else:
            print('no')
            break
    else:
        print('yes')




if __name__ == '__main__':
    N = int(input())
    l = [int(x) for x in input().split()]
    tupac(l, N)