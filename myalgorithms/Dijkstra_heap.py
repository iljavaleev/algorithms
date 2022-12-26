import heapq
from nodes_edges import Vertex


def DijkstraHeap(s, H):
    X = set()
    s.key = 0
    heapq.heapify(H)
    while H:
        w = heapq.heappop(H)
        X.add(w)
        w.value = w.get_key()
        for destination, weight in w.out_adj_list:
            destination.key = destination.get_key()
    return X


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
    X = DijkstraHeap(s, G)

    for i in X:
        print(i)

