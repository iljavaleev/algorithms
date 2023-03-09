import bisect

def find(diego, col):
    for i in col:
        print(bisect.bisect_left(diego, i))


if __name__ == '__main__':
    _ = input()
    diego = sorted({int(x) for x in input().split()})
    _ = input()
    col = [int(x) for x in input().split()]
    find(diego, col)