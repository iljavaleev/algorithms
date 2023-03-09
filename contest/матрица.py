def func(matrix, req, K):
    result = [0] * K
    for j in range(K):
        x1, y1, x2, y2 = req[j]
        for i in range(x1-1, x2):
            result[j] += sum(matrix[i][y1-1:y2])
    print(*result, sep='\n')


if __name__ == '__main__':
    N, M, K = [int(x) for x in input().split()]
    d_row = []
    req = []
    for i in range(N):
        d_row.append([int(x) for x in input().split()])
    for i in range(K):
        x1, y1, x2, y2 = [int(x) for x in input().split()]
        req.append((x1,y1,x2,y2))
    func(d_row, req, K)