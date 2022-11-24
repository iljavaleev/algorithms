def join(values, delimiter):
    res = ''
    for i in range(len(values) - 1):
        res += (values[i] + delimiter)

    return res + values[-1]


values = ['hello', 'world', 'message']
print(join(values, '+++'))



