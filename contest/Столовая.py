import math


def eat(data, dp, prev, N):
    for row in range(1, N + 1):
        for column in range(1, N + 2):
            if data[row] > 100:
                t11 = data[row] + dp[row - 1][column - 1]
                t21 = dp[row - 1][column + 1]
                if t21 < t11:
                    dp[row][column] = t21
                    prev[row][column] = (row - 1, column + 1)
                else:
                    dp[row][column] = t11
                    prev[row][column] = (row - 1, column - 1)
            else:
                t12 = data[row] + dp[row - 1][column]
                t22 = dp[row - 1][column + 1]
                if t22 < t12:
                    dp[row][column] = t22
                    prev[row][column] = (row - 1, column + 1)
                else:
                    dp[row][column] = t12
                    prev[row][column] = (row - 1, column)

    l = dp[-1]
    min, idx = math.inf, 0
    for i in range(len(l)):
        if l[i] <= min:
            min, idx = l[i], i

    print(dp[-1][idx])

    st_r, st_c = N, idx
    count = 0
    days = []
    while True:
        pr_row, pr_column = prev[st_r][st_c]
        if (pr_row, pr_column) == (-1, -1):
            break
        if pr_column > st_c:
            count += 1
            days.append(st_r)
        st_r, st_c = pr_row, pr_column
    print(idx - 1, count)
    print(*days[::-1])


if __name__ == '__main__':
    N = int(input())
    data = []
    for _ in range(N):
        data.append(int(input()))

    dp = [[math.inf] * (N + 3)] + [[math.inf] * (N + 3) for x in range(N)]
    prev = [[(-1, -1)] * (N + 3)] + [[(-1, -1)] * (N + 3) for x in range(N)]
    dp[0][1] = 0
    data = [0] + data
    eat(data, dp, prev, N)
