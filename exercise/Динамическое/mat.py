# def comb(n):
#     if n == 1:
#         print(2)
#     else:
#         print(2**n - (2*(n-2) - 1))
#
# if __name__ == '__main__':
# n = int(input())
#
# from itertools import product
#
# items = [0, 1]
# all = 2**n
# count = 0
# for item in product(items, repeat=n):
#     c = 0
#     for i in item:
#         if i == 1:
#             c += 1
#         else:
#             c = 0
#         if c == 3:
#             count += 1
#             break
# print(2**n - count)


def comb(dp, n):
    for i in range(6, len(dp)):
        dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
    print(dp[n])


if __name__ == '__main__':
    dp = [0] * 36
    dp[1] = 2
    dp[2] = 4
    dp[3] = 7
    dp[4] = 13
    dp[5] = 24
    comb(dp, int(input()))