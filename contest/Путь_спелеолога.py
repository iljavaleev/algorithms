from collections import deque


class Vertex:
    root = None

    def __init__(self, name):
        self.name = name
        self.adj_list = set()
        self.finish = False
        self.visited = False
        self.start = False
        self.len = 0

    def add_connection(self, destination):
        self.adj_list.add(destination)
        destination.adj_list.add(self)

    def __repr__(self):
        return f'{self.name}'


def put(vertex):
    Q = deque()
    Q.append(vertex)
    vertex.visited = True
    while Q:
        v = Q.popleft()
        for w in v.adj_list:
            if not w.visited:
                w.len = v.len + 1
                if w.finish:
                    return w.len
                w.visited = True
                Q.append(w)


if __name__ == '__main__':
    with open('input.txt') as f:
        n = int(next(f))
        g = [['#'] + list(line.strip()) + ['#'] for line in f if line != '\n']

    G = []
    for i in range(0, len(g), n):
        G.append([['#'] * (n + 2)] + g[i: i+n] + [['#'] * (n + 2)])


    G.append([['#'] * (n + 2) for _ in range(n + 2)])

    graph = {}
    for i in range(n):
        for j in range(1, n + 1):
            for k in range(1, n + 1):
                if G[i][j][k] != '#':
                    v = graph.setdefault((i, j, k), Vertex((i, j, k)))
                    if i == 0:
                        v.finish = True
                    if G[i][j][k] == 'S':
                        Vertex.root = v
                    for c1, c2, c3 in ((i, j, k + 1), (i, j, k - 1), (i, j - 1, k),
                              (i, j + 1, k), (i + 1, j, k)):
                        if G[c1][c2][c3] != '#':
                            neig = graph.setdefault((c1, c2, c3), Vertex((c1, c2, c3)))
                            graph[(i, j, k)].add_connection(neig)

    print(put(Vertex.root))
    # print(graph[(1, 2, 3)].adj_list)
    # print(graph[(2, 2, 3)].adj_list)
