def check_braces(text):
    text = list(text)
    n = len(text)
    i = 1
    while i < n:
        if not text:
            return True
        if ord(text[0]) == 41:
            return False
        elif ord(text[i]) == 41:
            del text[i-1]
            del text[i-1]
            n -= 2
            i = 1
            continue
        i += 1
    if n == 0:
        return True
    return False

print(check_braces('()()'))
print(check_braces('(()))((())'))
print(check_braces('(())'))
print(check_braces('((()'))