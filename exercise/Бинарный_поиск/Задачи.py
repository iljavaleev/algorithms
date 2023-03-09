"""
Есть N задач. В первый день решил K из них. В каждый последующий день
на одну задачу больше.
Найти количество дней
"""


def l_binary_search(N, k):
    arr = list(range(1, N+1))
    low = 0
    high = len(arr)

    while low < high:
        days = (low + high) // 2
        value = (k + (k + days - 1)) * days

        if value == N:
            return days

        if value > N:
            high = days - 1
        else:
            low = days + 1

    return low


def binary_search(array, query):
    # array.remove(43)
    print(array)
    low, high = 0, len(array) - 1
    while low <= high:
        mid = (high + low) // 2
        val = array[mid]
        if val == query:
            return mid

        if val < query:
            low = mid + 1
        else:
            high = mid - 1
    return array[low]


if __name__ == '__main__':
    N = 100
    k = 15
    res = binary_search(list(range(N)), 43)
    print(res)