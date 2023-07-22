import math


def read_input(n):
    A = [[int(x) for x in input().split()] for _ in range(n)]
    B = [[int(x) for x in input().split()] for _ in range(n)]
    C = [[0] * n for _ in range(n)]

    if not math.log2(n).is_integer():
        m = math.ceil(math.log2(n))
        m **= 2
        delta = m - n
        A = [x+[0] * delta for x in A]
        B = [x+[0] * delta for x in B]
        C = [x+[0] * delta for x in C]
        A.append([0] * m)
        B.append([0] * m)
        C.append([0] * m)
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


def summ_mat(a, b, c, n):
    '''
    a, b, c - список из четырех координат две по ряду две по колонне
    '''
    if n == 1:
        # по координатам определить номер ячейки
        C[c[0]][c[2]] = A[a[0]][a[2]] + B[b[0]][b[2]]
        return

    A11, A12, A21, A22 = divide(a)
    B11, B12, B21, B22 = divide(b)
    C11, C12, C21, C22 = divide(c)

    summ_mat(A11, B11, C11, n / 2)
    summ_mat(A12, B12, C12, n / 2)
    summ_mat(A21, B21, C21, n / 2)
    summ_mat(A22, B22, C22, n / 2)


if __name__ == '__main__':
    n = int(input())
    A, B, C, n = read_input(n)
    print(A)
    print(n)
    a, b, c = [[0, n-1, 0, n-1] for _ in range(3)]
    summ_mat(a, b, c, n)
    print(C)