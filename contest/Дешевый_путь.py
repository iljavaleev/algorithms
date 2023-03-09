import math

def cheap_way(data, dp, N, M):
    for row in range(1, N + 1):
        for column in range(1, M + 1):
            dp[row][column] = data[row][column] + min(dp[row - 1][column], dp[row][column - 1])
    return dp[N][M]


if __name__ == '__main__':
    N, M = [int(x) for x in input().split()]
    data = [[0] * (M + 1)] + \
           [[0] + [int(x) for x in input().split()] for _ in range(N)]
    dp = [[math.inf] * (M + 1)] + [[math.inf] + [0] * M for _ in range(N)]
    dp[0][0] = dp[0][1] = dp[1][0] = 0
    print(cheap_way(data, dp, N, M))