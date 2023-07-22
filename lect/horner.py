def horner(A, n, x):
    if n == 1:
        return A[-2] + A[-1]*x
    else:
        return A[len(A) - n - 1] + x * horner(A, n - 1, 2)


if __name__ == '__main__':
    A = [1, 2, 3, 4]
    print(horner(A, len(A) - 1, 2))

