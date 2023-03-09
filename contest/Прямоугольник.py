def func(l):
    x = sorted(l, key=lambda x: x[0])
    y = sorted(l, key=lambda x: x[1])
    min_x, max_x = x[0][0], x[-1][0]
    min_y, max_y = y[0][1], y[-1][1]
    print(min_x, min_y, max_x, max_y)

if __name__ == '__main__':
    n = int(input())
    l = [tuple(int(x) for x in input().split()) for _ in range(n)]
    func(l)
