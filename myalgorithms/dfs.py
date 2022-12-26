from nodes_edges import Vertex

# def is_empty(lst):
#     return not lst


def dfs_iterative(vertex: Vertex):
    S = []
    S.append(vertex)
    while S:
        v = S.pop()
        if not v.explored:
            v.explored = True
            for n in v.out_adj_list:
                S.append(n.destination)


def dfs_recursive(vertex: Vertex):
    vertex.explored = True
    for v, w in vertex.out_adj_list:
        if not v.explored:
            v.explored = True
            dfs_recursive(v)


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

    graph = [s, a, b, c, d, e]
    # dfs_iterative(graph[0])
    # for g in graph:
    #     print(g.explored)
    dfs_recursive(graph[0])
    for g in graph:
        print(g.explored)

