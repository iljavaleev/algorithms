from queue import Queue
from nodes_edges import Vertex
import math

def bfs(vertex: Vertex):
    Q = Queue()
    vertex.explored = True
    Q.put(vertex)
    while not Q.empty():
        v = Q.get()
        for w in v.adj_list:
            if not w.explored:
                w.explored = True
                Q.put(w)


def bfs_with_length(vertex: Vertex):
    """Add length as vertex.value."""
    Q = Queue()
    vertex.explored = True
    vertex.value = 0
    Q.put(vertex)
    while not Q.empty():
        v = Q.get()
        for w in v.adj_list:
            if not w.explored:
                w.explored = True
                w.value = v.value + 1
                Q.put(w)


def UCC(graph):
    """Add components search"""
    numCC = 0
    for vertex in graph:
        if not vertex.explored:
            numCC += 1
            vertex.explored = True
            Q = Queue()
            Q.put(vertex)
            while not Q.empty():
                v = Q.get()
                v.component = numCC
                for w in v.adj_list:
                    if not w.explored:
                        w.explored = True
                        Q.put(w)


if __name__ == '__main__':
    s = Vertex("s")
    a = Vertex("a")
    b = Vertex("b")
    c = Vertex("c")
    d = Vertex("d")
    e = Vertex("e")

    s.add_connection(a)
    s.add_connection(b)
    a.add_connection(c)
    a.add_connection(s)
    b.add_connection(c)
    b.add_connection(s)
    c.add_connection(a)
    c.add_connection(b)
    c.add_connection(e)
    c.add_connection(d)
    e.add_connection(c)
    e.add_connection(d)
    d.add_connection(b)

    s1 = Vertex("s1")
    a1 = Vertex("a1")
    s1.add_connection(a1)
    a1.add_connection(s1)

    c2 = Vertex("c2")
    d2 = Vertex("d2")
    e2 = Vertex("e2")
    c2.add_connection(d2)
    d2.add_connection(c2)
    d2.add_connection(e2)
    e2.add_connection(d2)

    graph = [s, a, b, c, d, e, s1, a1, c2, d2, e2]
    UCC(graph)
    for g in graph:
        print(g)



