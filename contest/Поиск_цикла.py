from enum import Enum


class Color(Enum):
    white = 1
    grey = 2
    black = 3


class Vertex:

    def __init__(self, name):
        self.name = name
        self.adj_list = list()
        self.parent = None
        self.color = Color.white
        self.stop = False

    def add_connection(self, destination):
        self.adj_list.append(destination)

    def __repr__(self):
        return f'{self.name}'


def dfs_iterative(v):
    S = []
    S.append(v)
    while S:
        v = S[-1]
        if v.color is not Color.grey:
            v.color = Color.grey
            for w in v.adj_list:
                if w.color is Color.white:
                    w.parent = v
                    S.append(w)
                elif w.color is Color.grey and w is not v.parent:
                    w.stop = True
                    return 'YES', v

        elif v.color is Color.grey:
            S.pop()
            v.color = Color.black


if __name__ == '__main__':

    with open('input1.txt') as f:
        n = int(next(f))
        G = [Vertex(i) for i in range(1, n + 1)]

        for idx, line in enumerate(f):
            row = [x for x in line.split()]
            for c in range(n):
                if row[c] == '1':
                    G[idx].add_connection(G[c])
    for v in G:
        r = dfs_iterative(v)
        if r is not None:
            a, l = r
            p = [l]
            while True:
                l = l.parent
                p.append(l)
                if l.stop:
                    break
            print(a)
            print(len(p))
            print(*p[::-1])
            break
    else:
        print('NO')
