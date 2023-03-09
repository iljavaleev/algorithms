def multiply_all_digits(value):
    remainder = value // 10
    digit_value = value % 10

    if remainder > 0:
        result = multiply_all_digits(remainder)
        return digit_value * result
    else:
        return value


if __name__ == '__main__':
    multiply_all_digits(1234)
