"""
Дана отсортированная последовательность чисел длиной N и число K
Найти количество пар чисел A, B таких что B - A > K
"""


def get_differ_pairs(nums, k):
    count = 0
    right = 0
    for left in range(len(nums)):
        while right < len(nums) and nums[right] - nums[left] <= k:
            right += 1
        count += len(nums) - right
    return count


if __name__ == '__main__':
    l = [1, 3, 7, 8]
    print(get_differ_pairs(l, 4))