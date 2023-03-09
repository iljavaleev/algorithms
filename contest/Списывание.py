from enum import Enum

class Type(Enum):
    t_1 = 1
    t_2 = 2

class Vertex:

    def __init__(self, name, type=None):
        self.name = name
        self.adj_list = list()
        self.explored_first = False
        self.explored_second = False
        self.type = type

    def add_connection(self, destination):
        self.adj_list.append(destination)
        destination.adj_list.append(self)

    def __lt__(self, other):
        return self.name < other.name

    def __eq__(self, other):
        return self.name == other.name


def dfs_comp(vertex: Vertex):
    S = []
    l = []
    S.append(vertex)
    while S:
        v = S.pop()
        if not v.explored_first:
            v.explored_first = True
            l.append(v)
            for n in v.adj_list:
                S.append(n)
    return l


def dfs_iterative(vertex: Vertex):
    S = []
    S.append(vertex)
    while S:
        v = S.pop()
        if not v.explored_second:
            v.explored_second = True
            for n in v.adj_list:
                if n.type == v.type:
                    return 'NO'
                if v.type == Type.t_1:
                    n.type = Type.t_2
                else:
                    n.type = Type.t_1
                S.append(n)
    return 'YES'


if __name__ == '__main__':
    v, e = (int(x) for x in input().split())
    G = [Vertex(i) for i in range(1, v + 1)]

    for _ in range(e):
        v, to = [int(x) for x in input().split()]
        G[v - 1].add_connection(G[to - 1])

    res = (dfs_comp(x) for x in G)
    comp = tuple(x for x in res if x)
    for c in comp:
        c[0].type = Type.t_1
        if dfs_iterative(c[0]) == 'NO':
            print('NO')
            break
    else:
        print('YES')

