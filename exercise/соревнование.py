def find_draw(l):
    if len(l) < 2:
        print(0)
        return
    print(len(l))
    while True:
        x = len(l)
        y = sum(l)
        if x/y == 2:
            print(x)
            break
        l = l[1:-1]

def find_draw(l):
    if len(l) < 2:
        print(0)
        return
    left = 0
    right = len(l)


    while True:
        x = len(l)
        y = sum(l)
        if x/y == 2:
            print(x)
            break
        if x/y > 2:
            if l[left] == 1:
                left+=1

        l = l[1:-1]



if __name__ == '__main__':
    # _ = input()
    # l = [int(x) for x in input().split()]
    # find_draw(l)
    print(ord('1'))
