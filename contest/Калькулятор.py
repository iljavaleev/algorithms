def calc(N, data, most_idx):
    for n in range(2, N + 1):
        t3, t2 = n, n
        if n % 3 == 0:
            t3 = data[n // 3]
        if n % 2 == 0:
            t2 = data[n // 2]

        data[n] = data[n - 1]
        most_idx[n] = n - 1
        if data[n] > t3:
            data[n] = t3
            most_idx[n] = n//3

        if data[n] > t2:
            data[n] = t2
            most_idx[n] = n // 2


        data[n] += 1


    print(data[N])
    way = []
    r = N
    while True:
        way.append(r)
        r = most_idx[r]
        if r == -1:
            break
    print(*way[::-1])


if __name__ == '__main__':
    N = int(input())
    data = [-1] * (N + 1)
    prev_idx = [-1] * (N + 1)
    data[0], data[1] = 0, 0
    prev_idx[0] = -1
    calc(N, data, prev_idx)
