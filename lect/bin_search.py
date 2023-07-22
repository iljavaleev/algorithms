def bin_search(l, k):
    left = 0
    right = len(l) - 1

    while left <= right:
        mid = (right + left) // 2
        if l[mid] == k:
            return mid
        elif k > l[mid]:
            left = mid + 1
        else:
            right = mid - 1

    return -1


if __name__ == '__main__':
    arr = [2, 3, 4, 10, 40]
    x = 10
    print(bin_search(arr, x))
