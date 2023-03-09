def check_braces(s):
    if len(s) < 2:
        return 'no'
    l = []
    for i in range(len(s)):
        if s[i] in {'{', '(', '['}:
            l.append(s[i])
        else:
            if len(l) > 0:
                br = l.pop()
            else:
                return 'no'
            if abs(ord(s[i]) - ord(br)) > 2:
                return 'no'
    if len(l) == 0:
        return 'yes'
    else:
        return 'no'

if __name__ == '__main__':
    s = input()
    print(check_braces(s))
