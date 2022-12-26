class Node:
    def __init__(self, value, root=False, parent=None, left=None, right=None):
        self.value = value
        self.parent = parent
        self.left = left
        self.right = right
        self.root = root

    def set_left(self, other):
        self.left = other
        if other is not None:
            other.parent = self

    def set_right(self, other):
        self.right = other
        if other is not None:
            other.parent = self

    def set_parent(self, parent):
        if parent is not None:
            if parent.left is self:
                parent.set_left(self)
            else:
                parent.set_right(self)
        else:
            self.parent = None

    def get_size(self):
        return Node._size(self)

    @staticmethod
    def _size(node):
        if node is None:
            return 0
        else:
            return Node._size(node.left) + 1 + Node._size(node.right)

    def print_v(self):
        print(f'^- {self.parent} -> {self.right} <- {self.left}')

    def __repr__(self):
        return self.value

    def __str__(self):
        return f'{self.value}'


class Search_Tree:
    def __init__(self, iter=None):
        if iter is None:
            self.tree = list()
        else:
            self.tree = list(iter)
            self.root = None
            for n in self.tree:
                if n.root:
                    self.root = n

    def search(self, value):
        return self._bin_search(self.root, value)

    def _bin_search(self, root, value):
        if root is None:
            return root

        if root.value == value:
            return root
        elif root.value > value:
            return self._bin_search(root.left, value)
        else:
            return self._bin_search(root.right, value)

    def _make_connection(self, for_delete, node=None):
        if for_delete.parent.left is for_delete:
            for_delete.parent.left = node
        else:
            for_delete.parent.right = node
        self._delete_connections(for_delete)

    def _delete_connections(self, vertex):
        vertex.left, vertex.right, vertex.parent = [None] * 3

    def delete(self, value):
        for_delete = self.search(value)
        if for_delete is None:
            raise ValueError('Object doesnt exists')
        else:
            self.tree.remove(for_delete)

            if for_delete.left is None and for_delete.right is None:
                if for_delete.root:
                    self.root = None
                self._make_connection(for_delete)

            elif for_delete.left is not None and for_delete.right is None:
                if for_delete.root:
                    for_delete.root = False
                    for_delete.left.root = True
                    self.root = for_delete.left.root
                    for_delete.left.parent = None
                else:
                    self._make_connection(for_delete, for_delete.left)

            elif for_delete.left is None and for_delete.right is not None:
                if for_delete.root:
                    for_delete.root = False
                    for_delete.right.root = True
                    self.root = for_delete.right.root
                    for_delete.right.parent = None
                else:
                    self._make_connection(for_delete, for_delete.right)

            else:
                predecessor = self.predecessor(for_delete)
                if for_delete.root:
                    predecessor.root = True
                    for_delete.root = False
                    self.root = predecessor

                fd_l, fd_r, fd_p = for_delete.left, for_delete.right, for_delete.parent
                pr_l, pr_p = predecessor.left, predecessor.parent

                if predecessor is for_delete.left:
                    predecessor.set_parent(fd_p)
                    predecessor.set_left(for_delete)
                else:
                    for_delete.set_parent(pr_p)
                    predecessor.set_left(fd_l)
                    predecessor.set_parent(fd_p)

                predecessor.set_right(fd_r)

                for_delete.set_left(pr_l)
                for_delete.set_right(None)

                for_delete.parent.set_right(for_delete.left)

                self._delete_connections(for_delete)

    def select(self, i):
        return self._select(self.root, i)

    def _select(self, root, i):
        if root.left is None:
            j = 0
        else:
            j = root.left.get_size()

        if i == j + 1:
            return root
        elif i < j + 1:
            return self._select(root.left, i)
        else:
            return self._select(root.right, i - j - 1)

    def insert(self, value):
        return self._insert_search(self.root, value)

    def _insert_search(self, root, value):
        if root is None:
            return root

        if root.value == value:
            n = Node(value)
            self.tree.append(n)
            left_child = root.left
            root.set_left(n)
            if left_child is not None:
                n.set_left(left_child)
            return n

        elif root.value > value:
            node = self._insert_search(root.left, value)
            if node is None:
                n = Node(value)
                self.tree.append(n)
                root.set_left(n)
                return n
            else:
                return node

        else:
            node = self._insert_search(root.right, value)
            if node is None:
                n = Node(value)
                self.tree.append(n)
                root.set_right(n)
                return n
            else:
                return node

    def min(self):
        return self._find_min(self.root)

    def _find_min(self, root):
        if root.left is None:
            return root
        else:
            return self._find_min(root.left)

    def max(self):
        return self._find_max(self.root)

    def _find_max(self, root):
        if root.right is None:
            return root
        else:
            return self._find_max(root.right)

    def predecessor(self, node):
        if node.left is not None:
            return self._find_max(node.left)
        else:
            return self._up_traverse_right(node)

    def _up_traverse_right(self, node):
        if node.parent is None:
            return None

        if node.parent.right is node:
            return node.parent
        else:
            return self._up_traverse_right(node.parent)

    def successor(self, node):
        if node.right is not None:
            return self._find_min(node.right)
        else:
            return self._up_traverse_left(node)

    def _up_traverse_left(self, node):
        if node.parent is None:
            return None

        if node.parent.left is node:
            return node.parent
        else:
            return self._up_traverse_left(node.parent)

    def output_sorted(self):
        res = []
        return self._output_sorted(self.root, res)

    def _output_sorted(self, root, res):
        if root is not None:
            res = self._output_sorted(root.left, res)
            res.append(root)
            res = self._output_sorted(root.right, res)
        return res

if __name__ == '__main__':
    n3 = Node(3, root=True)
    n1 = Node(1)
    n2 = Node(2)
    n4 = Node(4)
    n5 = Node(5)

    n3.set_left(n1)
    n3.set_right(n5)
    n1.set_right(n2)
    n5.set_left(n4)

    tree = [n1, n2, n3, n4, n5]

    s = Search_Tree(tree)
    # print(s.root.value)
    r = s.search(2)
    # print(r.parent.value)
    # print(s.min().value)
    # print(s.max().value)
    # print(s.successor(n5))

    # res = s.output_sorted()
    # for i in res:
    #     print(i)
    #
    res = s.insert(10)
    # n = s.tree[-1]

    # print(res)
    #
    # print()
    # res = s.output_sorted()
    # for i in res:
    #     print(i)

    # res = s.insert(7)

    # print()
    # res = s.output_sorted()
    # for i in res:
    #     print(i)

    # s = s.tree[-2:]
    # print()
    # # print(n5.right)
    # print(n5.left)
    # print()
    # print(n5.right)
    # s.insert(6)
    # s.delete(5)
    # print()
    # s.delete(3)


    #
    for i in s.tree:
        print(i)
    # s.delete(4)
    # n = s.tree[-7]
    # print(n.value)
    # n.print_v()
    #
    # print(n4.value)
    # print(n4.parent)
    # print(n4.left)
    # print(n4.right)
    # res = s.output_sorted()
    # for i in res:
    #     print(i)
    # print(n3.get_size())
    print()
    print(s.select(3))
