def white_king_pawn(board, i, j):
    if i == 0 or j - 1 < 0 or j + 1 > 7:
        return False
    if board[i-1][j-1] == 'p' or board[i-1][j+1] == 'p':
        return True
    return False


def black_king_pawn(board, i, j):
    if i == 7 or j - 1 < 0 or j + 1 > 7:
        return False
    if board[i+1][j-1] == 'P' or board[i+1][j+1] == 'P':
        return True
    return False


def king_bishop(board, n, m, color='white'):

    def check(board, i, j, color):
        pos = board[i][j]
        if (color == 'white' and (pos == 'b' or pos == 'q') or color == 'black'
                and (pos == 'B' or pos == 'Q')):
            return True
        elif board[i][j] != '.':
            return False

    i, j = n, m
    while i - 1 > 0 and j - 1 > 0:
        i -= 1
        j -= 1
        res = check(board, i, j, color)
        if res is not None:
            return res
    i, j = n, m
    while i - 1 > 0 and j + 1 <= 7:
        i -= 1
        j += 1
        res = check(board, i, j, color)
        if res is not None:
            return res
    i, j = n, m
    while i + 1 <= 7 and j - 1 > 0:
        i += 1
        j -= 1
        res = check(board, i, j, color)
        if res is not None:
            return res
    i, j = n, m
    while i + 1 > 0 and j + 1 <= 7:
        i += 1
        j += 1
        res = check(board, i, j, color)
        if res is not None:
            return res


def king_rook(board, n, m, color='white'):

    def check(board, i, j, color):
        pos = board[i][j]
        if (color == 'white' and (pos == 'r' or pos == 'q') or color == 'black'
                and (pos == 'R' or pos == 'Q')):
            return True
        elif board[i][j] != '.':
            return False

    i, j = n, m
    while i - 1 > 0:
        i -= 1
        res = check(board, i, j, color)
        if res is not None:
            return res
    i, j = n, m
    while j + 1 <= 7:
        j += 1
        res = check(board, i, j, color)
        if res is not None:
            return res
    i, j = n, m
    while i + 1 <= 7:
        i += 1
        res = check(board, i, j, color)
        if res is not None:
            return res
    i, j = n, m
    while j - 1 > 0:
        j -= 1
        res = check(board, i, j, color)
        if res is not None:
            return res


def king_knight(board, i, j, color='white'):
    def check_on(i, j):
        return -1 < i < 8 and -1 < j < 8
    neigth = ((i-1, j-2), (i-2, j-1), (i-1, j+2), (i-2, j+1), (i+1, j-2),
              (i+2, j-1), (i+1, j+2), (i+2, j+1))
    to_check = []
    for p in neigth:
        if check_on(*p):
            to_check.append(p)
    for n in to_check:
        figure = board[n[0]][n[1]]
        if color == 'white' and figure == 'n' or color == "black" and figure == 'N':
            return True
    return False


def check(chessboard, b, w):
    if (black_king_pawn(chessboard, *b)
            or king_bishop(chessboard, *b, color='black')
            or king_rook(chessboard, *b, color='black')
            or king_knight(chessboard, *b, color='black')):
        print('black king is in check')

    elif (black_king_pawn(chessboard, *w)
            or king_bishop(chessboard, *w)
            or king_rook(chessboard, *w)
            or king_knight(chessboard, *w)):
        print('white king is in check')

    else:
        print('no king is in check')


if __name__ == '__main__':
    chessboard = []
    black_king = None
    white_king = None

    for i in range(8):
        row = list(input())
        for j in range(8):
            if row[j] == 'k':
                black_king = i, j
            elif row[j] == 'K':
                white_king = i, j

        chessboard.append(row)

    check(chessboard, black_king, white_king)
