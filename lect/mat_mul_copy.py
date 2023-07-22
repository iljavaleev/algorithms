import math


def read_input(n):
    A = [[int(x) for x in input().split()] for _ in range(n)]
    B = [[int(x) for x in input().split()] for _ in range(n)]
    C = [[0] * n for _ in range(n)]

    if not math.log2(n).is_integer():
        m = math.ceil(math.log2(n))
        m = 2**m
        delta = m - n
        A = [x+[0] * delta for x in A]
        B = [x+[0] * delta for x in B]
        C = [x+[0] * delta for x in C]
        A.extend([[0] * m for _ in range(delta)])
        B.extend([[0] * m for _ in range(delta)])
        C.extend([[0] * m for _ in range(delta)])
        return A, B, C, m

    return A, B, C, n


def divide(M, n):

    m = n // 2
    A11 = [half[:m] for half in M[:m]]
    A12 = [half[m:] for half in M[:m]]
    A21 = [half[:m] for half in M[m:]]
    A22 = [half[m:] for half in M[m:]]

    return A11, A12, A21, A22


def combine(c11, c12, c21, c22):
    m, n = len(c11), len(c11) * 2
    C = [[0] * m for _ in range(n)]
    for i in range(m):
        C[i][:m] = c11[i]

    for i in range(m):
        C[i][m:] = c12[i]

    for i in range(m, n):
        C[i][:m] = c21[i-m]

    for i in range(m, n):
        C[i][m:] = c22[i-m]

    return C


def add_mat(A, B):
    n, m = len(A), len(A[0])
    C = [[0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            C[i][j] = A[i][j] + B[i][j]
    return C


def mat_mul_rec(A, B, n):
    '''
    a, b, c - список из четырех координат две по ряду две по колонне
    '''
    if n == 1:
        return [[A[0][0] * B[0][0]]]

    A11, A12, A21, A22 = divide(A, n)
    B11, B12, B21, B22 = divide(B, n)

    C11 = add_mat(mat_mul_rec(A11, B11, n // 2), mat_mul_rec(A12, B21, n // 2))
    C12 = add_mat(mat_mul_rec(A11, B12, n // 2), mat_mul_rec(A12, B22, n // 2))
    C21 = add_mat(mat_mul_rec(A21, B11, n // 2), mat_mul_rec(A22, B21, n // 2))
    C22 = add_mat(mat_mul_rec(A21, B12, n // 2), mat_mul_rec(A22, B22, n // 2))

    return combine(C11, C12, C21, C22)


def print_matrix(M):
    for i in range(len(M)):
        for j in range(len(M[0])):
            print(M[i][j], end=' ')
        print()


if __name__ == '__main__':
    n = int(input())
    A, B, _, n = read_input(n)
    C = mat_mul_rec(A, B, n)
    print_matrix(C)
