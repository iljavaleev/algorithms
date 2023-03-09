import math


def get_min(data, dp):
    for row in range(3, len(data)):
        a = data[row][0] + dp[row-1]
        b = data[row - 1][1] + dp[row - 2]
        c = data[row - 2][2] + dp[row - 3]
        dp[row] = min(a, b, c)
    print(dp[-1])


if __name__ == '__main__':
    n = int(input())
    data = [(0, 0, 0)] * 3
    data += [tuple(int(x) for x in input().split()) for _ in range(n)]

    dp = [math.inf] * 2 + [0] * (n + 1)
    get_min(data, dp)
