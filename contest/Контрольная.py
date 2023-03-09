def get(N, k, row, var):
    row_number = N // 2
    if var == 1:
        down = (row - 1) * 2 < k
        up = (row_number - row) * 2 + 1 < k
    else:
        down = (row - 1) * 2 + 1 < k
        up = (row_number - row) * 2 < k
    if down and up:
        print(-1)
    else:
        if not up:
            row += k // 2
        else:
            row -= k // 2
        if k % 2 == 0:
            return print(row, var)
        else:
            if var == 1:
                return print(row, var + 1)
            else:
                return print(row, var - 1)



if __name__ == '__main__':
    N = int(input())
    k = int(input())
    row = int(input())
    var = int(input())
    get(N, k, row, var)
