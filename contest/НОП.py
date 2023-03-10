def nop(dp, row, column, n, m):
    res = []
    maxi = 0
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
            if row[i] == column[j]:
                dp[i][j] += 1
                if dp[i][j] > maxi:
                    maxi = dp[i][j]
                    res.append(row[i])
    return dp[-1][-1], res



if __name__ == '__main__':
    n = int(input())
    row = [None] + [int(x) for x in input().split()]
    m = int(input())
    column = [None] + [int(x) for x in input().split()]
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    print(row, column)
    print(dp)
    print(nop(dp, row, column, n, m))