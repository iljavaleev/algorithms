def is_palindrome_simple_recursive(values):
    if len(values) <= 1:
        return True

    left = 0
    right = len(values) - 1

    if values[left] == values[right]:
        remainder = values[left+1:right]
        return is_palindrome_simple_recursive(remainder)

    return False


def is_palindrome_recursive_optimized(values):
    return is_palindrome_recursive_in_range(values, 0, len(values) - 1)


def is_palindrome_recursive_in_range(values, left, right):
    if left >= right:
        return True

    if values[left] == values[right]:
        return is_palindrome_recursive_in_range(values, left + 1, right - 1)

    return False

# iterative


def is_palindrome_iterative(values):
    left = 0
    right = len(values) - 1

    same_values = True

    while left < right and same_values:
        same_values = values[left] == values[right]
        left += 1
        right -= 1

    return same_values


def is_palindrome_iterative_compact(values):
    left = 0
    right = len(values) - 1
    while left < right and values[left] == values[right]:
        left += 1
        right -= 1
    # left >= right or values[left] != values[right]
    return left >= right


def is_palindrome_extension(values):
    values = values.lower()
    left = 0
    right = len(values) - 1

    same_values = True

    while left < right and same_values:

        if values[right] in ['!', '?']:
            right -= 1
            continue

        if values[left] == ' ':
            left += 1
        if values[right] == ' ':
            right -= 1

        same_values = values[left] == values[right]
        left += 1
        right -= 1

    return same_values

print(is_palindrome_extension('Was it a car or a cat I saw?'))