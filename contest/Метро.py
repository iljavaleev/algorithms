from collections import deque

class Vertex:
    strt = None

    def __init__(self, name):
        self.name = name
        self.adj_list = list()
        self.finish = False
        self.visited = False
        self.parent = self
        self.line = None

    def add_connection(self, destination):
        self.adj_list.append(destination)
        destination.adj_list.append(self)

    def __repr__(self):
        return f'{self.name}, line: {self.line}'


def min_len(vertex):
    Q = deque()
    Q.append(vertex)
    vertex.visited = True
    while Q:
        v = Q.popleft()
        for w in v.adj_list:
            if not w.visited:
                w.parent = v
                if w.finish:
                    return v
                w.visited = True
                Q.append(w)
    return -1


if __name__ == '__main__':
    n = int(input())
    lines = int(input())

    G = {}
    for i in range(1, n+1):
        G[i] = Vertex(i)

    for i in range(1, lines + 1):
        p, *l = [int(x) for x in input().split()]
        for j in range(p):
            if G[l[j]].line is None:
                G[l[j]].line = i
            G[l[j]].add_connection(G[l[j-1]])

    A, B = [int(x) for x in input().split()]
    G[B].finish = True

    Vertex.strt = G[A]
    w = min_len(Vertex.strt)
    if w == -1:
        print(-1)
    else:
        count = 0
        while w.parent != w:
            v = w.parent
            # print(v.line)
            if v.line != w.line:
                count += 1
            w = v
        print(count)