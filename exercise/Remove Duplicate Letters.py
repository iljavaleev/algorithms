def remove_duplicates(text):
    l = list(text)
    res = []
    for i in l:
        if not i.lower() in res and not i.upper() in res:
            res.append(i)
    return ''.join(res)


print(remove_duplicates('AaBbcCdD'))

print(ord('i'), ord('I'))