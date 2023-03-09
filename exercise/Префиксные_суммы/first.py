'''
Массив  nums и число N. Чему равна сумма элементов в полуинтервале [L, R)

prefix[i] = prefix[i-1] + nums[i-1]

len(prefix) = len(nums) + 1
sum(L, R) = prefix(R) - prefix(L) - сумма в диапазоне [L, R)
'''


def make_prefix_sum(nums):
    prefixsum = [0] * (len(nums) + 1)
    for i in range(1, len(nums) + 1):
        prefixsum[i] = prefixsum[i-1] + nums[i-1]
    return prefixsum


def rsq(prefixsum, l, r):
    return prefixsum[r] - prefixsum[l]

"""
Дана последовательность чисел длиной N и M запросов.
Сколько нулей на полуинтервале[L, R )
"""


def make_prefix_sum_zeros(nums):
    prefixsum = [0] * (len(nums) + 1)
    for i in range(1, len(nums) + 1):
        if nums[i-1] == 0:
            prefixsum[i] = prefixsum[i-1] + 1
        else:
            prefixsum[i] = prefixsum[i - 1]
    return prefixsum


def zeros_rsq(prefixsum, l, r):
    return prefixsum[r] - prefixsum[l]


if __name__ == '__main__':
    s = '012034500055503'
    s = [int(x) for x in s]
    pr = make_prefix_sum_zeros(s)
    print(pr)
    print(zeros_rsq(pr, 0, 4))