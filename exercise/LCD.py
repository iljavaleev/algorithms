def print_some(s, b):
    for i in range(1, 6):
        if i == 1:
            for n in b:
                if n in [1, 4]:
                    print(*([' ']*(s+2)), end=' ')
                else:
                    print(*([' ']+['-']*s + [' ']), end=' ')
            print()
        elif i == 3:
            for n in b:
                if n in [1, 7, 0]:
                    print(*([' ']*(s+2)), end=' ')
                else:
                    print(*([' ']+['-']*s + [' ']), end=' ')
            print()
        elif i == 5:
            for n in b:
                if n in [1, 4, 7]:
                    print(*([' ']*(s+2)), end=' ')
                else:
                    print(*([' ']+['-']*s + [' ']), end=' ')
            print()
        elif i == 2:
            for _ in range(s):
                for n in b:
                    if n in [1, 2, 3, 7]:
                        print(*([' '] * (s + 1) + ['|']), end=' ')
                    elif n in [5, 6]:
                        print(*(['|'] + [' '] * (s + 1)), end=' ')
                    else:
                        print(*(['|'] + [' '] * s + ['|']), end=' ')
                print()
        else:
            for _ in range(s):
                for n in b:

                    if n == 2:
                        print(*(['|'] + [' '] * (s + 1)), end=' ')
                    elif n in [0, 6, 8]:
                        print(*(['|'] + [' '] * s + ['|']), end=' ')
                    else:
                        print(*([' '] * (s + 1) + ['|']), end=' ')
                print()

if __name__ == '__main__':
    s, b = input().split()
    b = [int(x) for x in list(b)]
    s = int(s)
    print_some(s, b)
