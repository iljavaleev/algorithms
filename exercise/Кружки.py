
if __name__ == '__main__':
    n = int(input())
    l = []
    for _ in range(n):
        l.append(input())
    for i in dict.fromkeys(l).keys():
        print(i)
