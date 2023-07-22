if __name__ == '__main__':
    n = int(input())
    time = [x.split(':') for x in input().split()]
    l = [int(x)*60 + int(y) for x, y in time]
    l.sort()


    mini = 1440 + l[0] - l[-1]
    for i in range(1, n):
        delta = l[i] - l[i - 1]
        if delta < mini:
            mini = delta
    print(mini)


