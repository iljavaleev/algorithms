from collections import deque


class Vertex:

    def __init__(self, name):
        self.name = name
        self.adj_list = list()
        self.finish = False
        self.visited = False
        self.len = 0

    def add_connection(self, destination):
        self.adj_list.append(destination)

    def __repr__(self):
        return f'{self.name}'


def min_len(vertex):
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
    return -1


if __name__ == '__main__':

    with open('input.txt') as f:
        n = int(next(f))
        G = [Vertex(i) for i in range(1, n + 1)]

        for idx in range(n):
            row = [x for x in f.readline().split()]
            for c in range(n):
                if row[c] == '1':
                    G[idx].add_connection(G[c])

        start, finish = [int(x) for x in next(f).split()]
        if start == finish:
            print(0)
        else:
            G[finish - 1].finish = True
            print(min_len(G[start - 1]))
