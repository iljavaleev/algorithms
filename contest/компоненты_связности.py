class Vertex:

    def __init__(self, name):
        self.name = name
        self.adj_list = list()
        self.explored = False

    def add_connection(self, destination):
        self.adj_list.append(destination)
        destination.adj_list.append(self)

    def __lt__(self, other):
        return self.name < other.name

    def __eq__(self, other):
        return self.name == other.name


def dfs_iterative(vertex: Vertex):
    S = []
    l = []
    S.append(vertex)
    while S:
        v = S.pop()
        if not v.explored:
            v.explored = True
            l.append(v)
            for n in v.adj_list:
                S.append(n)
    return l

if __name__ == '__main__':
    v, e = (int(x) for x in input().split())
    G = [Vertex(i) for i in range(1, v + 1)]

    for _ in range(e):
        v, to = [int(x) for x in input().split()]
        G[v-1].add_connection(G[to-1])

    res = (dfs_iterative(x) for x in G)
    res = tuple(x for x in res if x[0] != 0)
    print(len(res))
    for l, c in res:
        print(l)
        print(*c)


