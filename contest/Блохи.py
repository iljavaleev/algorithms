from collections import deque


def bfs(G, s: tuple, N, M):
    Q = deque()
    Q.append(s)

    visits = [[False] * (M + 1) for _ in range(N + 1)]
    lens = [[None] * (M + 1) for _ in range(N + 1)]
    visits[s[0]][s[1]] = True
    lens[s[0]][s[1]] = 0

    while Q:
        vi, vj = Q.popleft()
        for w in ((vi + 1, vj - 2), (vi - 1, vj + 2),
                  (vi - 1, vj - 2), (vi + 1, vj + 2),
                  (vi + 2, vj - 1), (vi - 2, vj + 1),
                  (vi + 2, vj + 1), (vi - 2, vj - 1)):
            if w in G and not visits[w[0]][w[1]]:
                lens[w[0]][w[1]] = 1 + lens[vi][vj]
                visits[w[0]][w[1]] = True
                Q.append(w)

    return lens


if __name__ == '__main__':
    N, M, S, T, Q = (int(x) for x in input().split())
    G = set()
    for i in range(1, N + 1):
        for j in range(1, M + 1):
            G.add((i, j))

    v = (S, T)
    lens = bfs(G, v, N, M)
    summ = 0
    for _ in range(Q):
        blox = tuple(int(x) for x in input().split())
        add = lens[blox[0]][blox[1]]
        if add is None:
            summ = -1
            break
        elif v == blox:
            continue
        else:
            summ += add
    print(summ)
