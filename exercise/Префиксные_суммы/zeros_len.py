'''
Дана последовательность чисел длиной N.
Найти количество отрезков с нулевой суммой
'''
from math import factorial

def count_zeros_range_cube(nums: list) -> int:
    count = 0
    for i in range(len(nums)):
        for j in range(i + 1, len(nums) + 1):
            range_sum = 0
            for k in range(i, j):
                range_sum += nums[k]
            if range_sum == 0:
                count += 1
    return count


def count_zeros_range_square(nums: list) -> int:
    count = 0
    for i in range(len(nums)):
        range_sum = 0
        for j in range(i, len(nums)):
            range_sum += nums[j]
            if range_sum == 0:
                count += 1
            else:
                break
    return count


def count_prefix(nums: list) -> dict:
    prefix_sum_by_value = {0: 1}
    now_sum = 0
    for now in nums:
        now_sum += now
        prefix_sum_by_value[now_sum] \
            = prefix_sum_by_value.setdefault(now_sum, 0) + 1
    print(prefix_sum_by_value)
    return prefix_sum_by_value


def count_zeros_range_prefix(nums: list) -> int:
    count = 0
    prefix_sum_by_value = count_prefix(nums)
    for nowsum in prefix_sum_by_value:
        count_sum = prefix_sum_by_value[nowsum]
        count += count_sum * (count_sum - 1) // 2 # выбор пары из n + 1 нулей или m одинаковых префиксных сумм
    return count


if __name__ == '__main__':
    l = [1, 0, 0, 0, 2, 4, 5, 0, 0, 12, 0, 0, 12, 2, 0, 0, 0, 12]
    r = count_zeros_range_prefix(l)
    print(r)
    print(factorial(3)*2 + factorial(2)*2)