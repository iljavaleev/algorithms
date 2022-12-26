from nodes_edges import Vertex
from topological import topo_sort
import random


def kosaraju(G):
    G = topo_sort(G, reversed=True) # find sink
    numSCC = 0
    for g in G:
        g.explored = False # all unexplored

    for vertex in G:
        if not vertex.explored:
            numSCC += 1
            dfs_scc(vertex, numSCC)


def dfs_scc(vertex, numSCC):
    vertex.explored = True
    vertex.component = numSCC
    for v, w in vertex.out_adj_list:
        if not v.explored:
            dfs_scc(v, numSCC)


if __name__ == '__main__':
    a = Vertex("1")
    b = Vertex("2")
    c = Vertex("3")
    d = Vertex("4")
    e = Vertex("5")
    f = Vertex("6")
    g = Vertex("7")
    h = Vertex("8")
    i = Vertex("9")
    j = Vertex("10")
    k = Vertex("11")

    a.add_connection(c)
    c.add_connection(e)
    e.add_connection(a)
    e.add_connection(i)
    e.add_connection(g)

    c.add_connection(k)
    k.add_connection(f)
    k.add_connection(h)

    j.add_connection(h)
    h.add_connection(f)
    f.add_connection(j)

    i.add_connection(b)
    i.add_connection(d)
    i.add_connection(h)
    b.add_connection(d)
    b.add_connection(j)
    d.add_connection(g)
    g.add_connection(i)

    G = [f, g, h, i, j, k, a, b, c, d, e]
    random.shuffle(G)
    kosaraju(G)

    for i in G:
        print(i)
