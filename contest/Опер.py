def cross(t):
    count = 1
    t = sorted(t)
    for i in range(1, len(t)):
        if t[i][0] > t[i-1][1]:
            count += 1
    print(count)


if __name__ == '__main__':
    M = int(input())
    N = int(input())
    t = []
    for i in range(N):
        t.append(tuple(int(x) for x in input().split()))
    print(sorted(t))
    cross(t)