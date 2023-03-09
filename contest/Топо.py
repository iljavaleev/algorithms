import math
from enum import Enum


class Color(Enum):
    white = 0
    gray = 1
    black = 2


class Vertex:

    def __init__(self, name):
        self.name = name
        self.out_adj_list = set()
        self.in_adj_list = set()
        self.explored = False
        self.color = Color.white

    def add_connection(self, destination):
        self.out_adj_list.add(destination)
        destination.in_adj_list.add(self)

    def __hash__(self):
        return hash(self.name)

    def __repr__(self):
        return f'{self.name}'

# change adj to list
def dfs_topo(v, cur_label, sorted_G):
    v.explored = True
    v.color = Color.gray

    for w in v.out_adj_list:
        if w.color == Color.gray:
            return cur_label, None
        if not w.explored:
            cur_label, sorted_G = dfs_topo(w, cur_label, sorted_G)

    v.value = cur_label
    v.color = Color.black
    if sorted_G is not None:
        sorted_G[cur_label-1] = v
    cur_label -= 1

    return cur_label, sorted_G


def topo_iterative(G: set[Vertex]) -> list | None:
    S = []
    while G:
        st_l = len(G)
        for v in G.copy():
            if not v.in_adj_list:
                S.append(v)
                for w in v.out_adj_list:
                    w.in_adj_list.remove(v)
                G.remove(v)
        if st_l == len(G):
            return None
    return S


if __name__ == '__main__':
    v, e = (int(x) for x in input().split())
    G = [Vertex(i) for i in range(1, v + 1)]
    for _ in range(e):
        v, to = [int(x) for x in input().split()]
        G[v - 1].add_connection(G[to - 1])

    G = set(G)
    r = topo_iterative(G)
    if r is not None:
        print(*[x.name for x in r])
    else:
        print('-1')


