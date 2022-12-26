from nodes_edges import Vertex
import math
import heapq

def dijkstra(s):
    X = [s]
    s.value = 0
    while True:
        for v in X:
            min, min_edge = math.inf, None
            for destination, weight in v.out_adj_list:
                if not destination in X:
                    length = v.value + weight
                    if length < min:
                        min = length
                        min_edge = destination
            if not min_edge:
                return False
            min_edge.value = min
            X.append(min_edge)

# def dijkstra(s):
#     X = [s]
#     s.value = 0
#     for v in X:
#         adj = sorted(v.out_adj_list, key=lambda x: x.weight)
#         if adj:
#             w, weight = adj[0]
#             if not w in X:
#                 w.value = weight + v.value
#                 X.append(w)


if __name__ == "__main__":
    s = Vertex("s")
    v = Vertex("v")
    w = Vertex("w")
    t = Vertex("t")

    s.add_connection(v, 1)
    v.add_connection(t, 6)
    v.add_connection(w, 2)
    s.add_connection(w, 4)
    w.add_connection(t, 3)

    G = [v, t, s, w]

    dijkstra(s)

    for i in G:
        print(i)
    s.value = 0

    print(v.key)
    print(w.get_key())
