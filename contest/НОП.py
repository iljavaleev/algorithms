def nop(dp, row, column, n, m):

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if row[i] == column[j]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    res = dp[n][m]
    p = []
    while res != 0:
        if res == dp[n - 1][m] and dp[n][m - 1]:
            n = n - 1
        else:
            p.append(row[n])
            n = n - 1
            m = m - 1
        res = dp[n][m]
    print(*p[::-1])

if __name__ == '__main__':
    n = int(input())
    row = [None] + [int(x) for x in input().split()]
    m = int(input())
    column = [None] + [int(x) for x in input().split()]
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    nop(dp, row, column, n, m)

