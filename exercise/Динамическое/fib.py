# classic
def fib(n):
    if n < 2:
        return 1
    return fib(n-1) + fib(n-2)


# dynamic
def fib_d(n, data):
    if data[n] == -1:
        data[n] = fib_d(n-1, data) + fib_d(n-2, data)
    return data[n]


def fib_d_i(n, data):
    for n in range(2, n+1):
        data[n] = data[n-1] + data[n-2]
    return data[n]


if __name__ == '__main__':
    n = int(input())
    data = [-1] * (n + 1)
    data[0] = data[1] = 1
    print(fib_d(n, data))
