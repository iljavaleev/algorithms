import math


def max_way(data, dp, N, M):
    for row in range(1, N + 1):
        for column in range(1, M + 1):
            if dp[row - 1][column] > dp[row][column - 1]:
                max = dp[row - 1][column]
                prev[row][column] = ('D', (row - 1, column))
            else:
                max = dp[row][column - 1]
                prev[row][column] = ('R', (row, column - 1))
            dp[row][column] = data[row][column] + max

    l = []
    prev[1][1] = -1
    row = N
    column = M
    while prev[row][column] != -1:
        fr, (r, c) = prev[row][column]
        l.append(fr)
        row, column = r, c
    print(dp[N][M])
    print(*l[::-1])


if __name__ == '__main__':
    N, M = [int(x) for x in input().split()]
    data = [[0] * (M + 1)] + \
           [[0] + [int(x) for x in input().split()] for _ in range(N)]
    dp = [[-math.inf] * (M + 1)] + [[-math.inf] + [0] * M for _ in range(N)]
    dp[0][0] = dp[0][1] = dp[1][0] = 0
    prev = [[0] * (M + 1)] + [[0] + [0] * M for _ in range(N)]
    prev[0][0] = prev[0][1] = prev[1][0] = -1
    max_way(data, dp, N, M)