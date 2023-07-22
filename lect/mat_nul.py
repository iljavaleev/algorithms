from mat_mul_rec import read_input, print_matrix


def mat_mul(A, B, C, n):
    for i in range(n):
        for j in range(n):
            for k in range(n):
                C[i][j] += A[i][k] * B[k][j]


if __name__ == '__main__':
    n = int(input())
    A, B, C, n = read_input(n)
    mat_mul(A, B, C, n)
    print_matrix(C)
