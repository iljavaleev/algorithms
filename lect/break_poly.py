if __name__ == '__main__':
    s = list(input())

    res = None

    if len(s) == 1:
        res = ''
    else:
        for i in range(len(s)//2):
            if ord(s[i]) > 97:
                s[i] = 'a'
                res = ''.join(s)
                break
        else:
            s[-1] = 'b'
            res = ''.join(s)
    print(res)