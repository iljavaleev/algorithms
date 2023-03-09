def max_len1(L):
    count = 0
    while set(L) != {0}:
        for i in range(len(L)):
            if L[i] != 0:
                L[i] -= 1
                count += 1
            else:
                continue
        count -= 1
    print(count)



def max_len2(L):
   



if __name__ == '__main__':
    N = int(input())
    l = list()
    for i in range(N):
        l.append(int(input()))
    print(l)