def fib(n):

    if n == 2 or n == 1:
        return 1

    return fib(n - 1) + fib(n - 2)


from array import  array


def it_fib(n: int) -> int:
    l = array('I', [0]) * n
    l[0], l[1] = 1, 1

    for i in range(2, n):
        l[i] = l[i - 1] + l[i - 2]

    return l[-1]


if __name__ == '__main__':
    # for i in range(1, 10):
    #     print(fib(i))

    print(it_fib(8))
