def count(dp, N, M):
    for row in range(2, N + 2):
        for column in range(2, M + 2):
            if dp[row - 2][column - 1] is not None:
                dp[row][column] += dp[row - 2][column - 1]
            if dp[row - 1][column - 2] is not None:
                dp[row][column] += dp[row - 1][column - 2]
    print(dp[N + 1][M + 1])


if __name__ == '__main__':
    N, M = [int(x) for x in input().split()]
    dp = [[None] * (M + 2) for _ in range(2)] + [[None, None] + [0] * M for _ in range(N)]
    dp[2][2] = 1
    count(dp, N, M)