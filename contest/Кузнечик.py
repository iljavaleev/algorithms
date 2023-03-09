def res(N , k):
    base = [0] * k
    base[-1] = 1
    data = base + [0] * (N - 1)
    for i in range(k, len(data)):
        data[i] = sum(data[i-k:i])
    print(data[-1])


if __name__ == '__main__':
    N, k = [int(x) for x in input().split()]
    res(N, k)