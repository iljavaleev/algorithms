from nodes_edges import Vertex


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
    i.add_connection(g)

    c.add_connection(k)
    k.add_connection(f)
    k.add_connection(h)

    j.add_connection(h)
    j.add_connection(f)
    h.add_connection(f)

    i.add_connection(b)
    i.add_connection(d)
    b.add_connection(d)
    d.add_connection(g)
    g.add_connection(i)

