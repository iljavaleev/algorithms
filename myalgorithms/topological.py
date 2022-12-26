from nodes_edges import Vertex


def dfs_topo(v, cur_label, sorted_G, rev):
    v.explored = True
    adj_list = (vertex.destination for vertex in v.out_adj_list)
    if rev:
        adj_list = (vertex.destination for vertex in v.in_adj_list)

    for w in adj_list:
        if not w.explored:
            cur_label, sorted_G = dfs_topo(w, cur_label, sorted_G, rev)
    v.value = cur_label
    sorted_G[cur_label-1] = v
    cur_label -= 1

    return cur_label, sorted_G


def topo_sort(G, reversed=False):
    sorted_G = [0] * len(G)
    cur_label = len(G)
    for v in G:
        if not v.explored:
            cur_label, sorted_G = dfs_topo(v,
                                           cur_label,
                                           sorted_G,
                                           rev=reversed)

    return sorted_G


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

    G = topo_sort(G, reversed=True)

    for g in G:
        print(f'{g.name} : {g.value}')
