def is_binary_number(number):
    return len(set(number)) <= 2

number = '10101'

assert is_binary_number(number) == True

def binary_to_decimal(number):
    n = len(number)
    number = list(number)
    result = 0
    if is_binary_number(number):
        for i in range(n - 1, -1, -1):
            result += 2 ** i * int(number[n - i - 1])
    else:
        raise ValueError
    return result

print(binary_to_decimal('1010011'))


def hex_to_decimal(number):
    keys = {"A": 10, "B": 11, "C": 12, "D": 13, "E": 14, "F": 15}
    n = len(number)
    number = list(number)
    result = 0
    if is_binary_number(number):
        for i in range(n - 1, -1, -1):
            symbol = number[n - i - 1]
            if symbol in keys:
                result += 16 ** i * keys[symbol]
            else:
                result += 16 ** i * int(number[n - i - 1])
    else:
        raise ValueError
    return result


print(hex_to_decimal('AB'))
