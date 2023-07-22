if __name__ == '__main__':
    path = [x for x in input().split('/') if x]
    res = []
    for i in range(len(path)):
        s = path[i]
        if s == '..':
            if res:
                res.pop()
            continue
        if s == '.':
            continue
        res.append(s)
    print('/' + '/'.join(res))





