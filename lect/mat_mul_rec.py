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


def divide(a):
    l, r, t, b = a
    m_i = (r + l) // 2
    m_j = (b + t) // 2

    A11 = [l, m_i, t, m_j]
    A21 = [m_i + 1, r, t, m_j]
    A12 = [l, m_i, m_j + 1, b]
    A22 = [m_i + 1, r, m_j + 1, b]

    return A11, A12, A21, A22


def mat_mul_rec(a, b, c, n):
    '''
    a, b, c - список из четырех координат две по ряду две по колонне
    '''
    if n == 1:
        # по координатам определить номер ячейки
        C[c[0]][c[2]] += A[a[0]][a[2]] * B[b[0]][b[2]]
        return

    A11, A12, A21, A22 = divide(a)
    B11, B12, B21, B22 = divide(b)
    C11, C12, C21, C22 = divide(c)

    mat_mul_rec(A11, B11, C11, n / 2)
    mat_mul_rec(A11, B12, C12, n / 2)
    mat_mul_rec(A21, B11, C21, n / 2)
    mat_mul_rec(A21, B12, C22, n / 2)

    mat_mul_rec(A12, B21, C11, n / 2)
    mat_mul_rec(A12, B22, C12, n / 2)
    mat_mul_rec(A22, B21, C21, n / 2)
    mat_mul_rec(A22, B22, C22, n / 2)


def print_matrix(M):
    for i in range(len(M)):
        for j in range(len(M[0])):
            print(M[i][j], end=' ')
        print()


if __name__ == '__main__':
    n = int(input())
    A, B, C, n = read_input(n)
    a, b, c = [[0, n-1, 0, n-1] for _ in range(3)]
    mat_mul_rec(a, b, c, n)
    print_matrix(C)
'''
[[54, 42, 312, 168], [18, 54, 168, 168], [22, 10, 168, 48], [14, 50, 48, 204]]

45 57 69 15 27 39 0 0 
81 102 123 24 45 66 0 0 
117 147 177 33 63 93 0 0 
63 84 105 33 54 75 0 0 
45 57 69 15 27 39 0 0 
81 102 123 24 45 66 0 0 
0 0 0 0 0 0 0 0 
0 0 0 0 0 0 0 0 

'''