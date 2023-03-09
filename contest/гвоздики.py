def min_l(data, dp):
    for i in range(2, len(dp)):
        dp[i] = min(dp[i - 1], dp[i - 2]) + data[i] - data[i - 1]
    return dp[-1]


if __name__ == '__main__':
    x = int(input())
    data = sorted([int(x) for x in input().split()])
    dp = [0] * x
    dp[0] = dp[1] = data[1] - data[0]
    print(min_l(data, dp))
