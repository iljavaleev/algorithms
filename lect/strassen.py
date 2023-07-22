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


def add_to(m, M, C):
    l, r, t, b = m
    for i in range(t, b+1):
        for j in range(l, r+1):
            C[i][j] += M[i-t][j-l]


def copy(m, M, minus=0):
    S = [[0] * n for _ in range(n)]
    l, r, t, b = m
    for i in range(t, b + 1):
        for j in range(l, r + 1):
            if minus:
                S[i - t][j - l] = M[i][j] * (-1)
            else:
                S[i - t][j - l] = M[i][j]
    return S


def divide(m):
    l, r, t, b = m
    m_i = (r + l) // 2
    m_j = (b + t) // 2

    M11 = [l, m_i, t, m_j]
    M21 = [m_i + 1, r, t, m_j]
    M12 = [l, m_i, m_j + 1, b]
    M22 = [m_i + 1, r, m_j + 1, b]

    return M11, M21, M12, M22


def sum_mat(m, M, B, n):
    '''
    a, b, c - список из четырех координат две по ряду две по колонне
    '''
    S = [[0]*n for _ in range(n)]
    l, r, t, b = m
    for i in range(t, b + 1):
        for j in range(l, r + 1):
            S[i - t][j - l] = M[i][j] + B[i - t][j - l]
    return S


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

    S1 = sum_mat(B12, B, copy(B21, B, minus=1), n//2)
    S2 = sum_mat(A11, A, copy(A12, A), n//2)
    S3 = sum_mat(A21, A, copy(A22, A), n//2)
    S4 = sum_mat(B21, B, copy(B11, B, minus=1), n//2)
    S5 = sum_mat(A11, A, copy(A22, A), n//2)
    S6 = sum_mat(B11, B, copy(B22, B), n//2)
    S7 = sum_mat(A12, A, copy(A22, A, minus=1), n//2)
    S8 = sum_mat(B12, B, copy(B22, B), n//2)
    S9 = sum_mat(A11, A, copy(A21, A, minus=1), n//2)
    S10 = sum_mat(B11, B, copy(B12, B), n//2)

    P = [[0] * n for _ in range(n//2)]

    P1 = mat_mul_rec(copy(A11, A), B11, C11, n / 2)
    P2 = mat_mul_rec(A11, B12, C12, n / 2)
    P3 = mat_mul_rec(A21, B11, C21, n / 2)
    P4 = mat_mul_rec(A21, B12, C22, n / 2)

    P5 = mat_mul_rec(A12, B21, C11, n / 2)
    P6 = mat_mul_rec(A12, B22, C12, n / 2)
    P7 = mat_mul_rec(A22, B21, C21, n / 2)

    return C


def print_matrix(M):
    for i in range(len(M)):
        for j in range(len(M[0])):
            print(M[i][j], end=' ')
        print()


if __name__ == '__main__':
    n = int(input())
    A, B, C, n = read_input(n)
    print(A)
    print(n)
    a, b, c = [[0, n-1, 0, n-1] for _ in range(3)]
    mat_mul_rec(a, b, c, n)
    print(C)
    multiple_of_one(A)
    print(A)
    # A = [[int(x) for x in input().split()] for _ in range(n)]
    # B = [[int(x) for x in input().split()] for _ in range(n//2)]
    # m = [0, 1, 2, 3]
    # add_to(m, B, A)
    # add_to(m, B, A)
    # print_matrix(A)
'''
[[54, 42, 312, 168], [18, 54, 168, 168], [22, 10, 168, 48], [14, 50, 48, 204]]
'''