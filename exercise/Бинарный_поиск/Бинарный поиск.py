def binary_search(array, query):

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
    return None


def binary_search_recur(array, low, high, val):
    if low > high:       # error case
        return -1

    mid = (low + high) // 2
    if val < array[mid]:
        return binary_search_recur(array, low, mid - 1, val)
    if val > array[mid]:
        return binary_search_recur(array, mid + 1, high, val)
    return mid
