def max_l(S):
    prev = 0
    i = 1
    maxl = 0
    if len(S) == 1:
        return 1

    while i < len(S):
        idx = S.find(S[i], prev, i)
        if idx != -1:
            prev = idx + 1
            diff = i - idx
        else:
            diff = i - prev + 1
        if diff > maxl:
            maxl = diff

        i += 1
    return maxl


if __name__ == '__main__':
    s = input()
    print(max_l(s))
    # s = 'ab'
    # print(s.find(s[1],0, 2))