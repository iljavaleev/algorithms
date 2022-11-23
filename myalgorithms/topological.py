from nodes_edges import Vertex


def dfs_topo(v, cur_label):
    v.explored = True
    for w in v.adj_list:
        if not w.explored:
            cur_label = dfs_topo(w, cur_label)
    v.value = cur_label
    cur_label -= 1

    return cur_label


def topo_sort(G):
    cur_label = len(G)
    for v in G:
        if not v.explored:
            cur_label = dfs_topo(v, cur_label)


if __name__ == '__main__':
    s = Vertex("s")
    v = Vertex("v")
    w = Vertex("w")
    t = Vertex("t")

    s.add_connection(v)
    v.add_connection(t)
    s.add_connection(w)
    w.add_connection(t)

    G = [v, t, s, w]

    topo_sort(G)

    for g in G:
        print(f'{g.name} : {g.value}')