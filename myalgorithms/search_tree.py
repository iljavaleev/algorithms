from __future__ import annotations
from enum import Enum
from typing import Optional, Union


class Color(Enum):
    RED = 1
    BLACK = 2


class Node:
    def __init__(self, value: int = None, root: bool = False,
                 parent: Node = None, left: Node = None, right: Node = None,
                 color: Color = Color.BLACK):
        self.value = value
        self.parent = parent
        self.left = left
        self.right = right
        self.root = root
        self.color = color

    def set_left(self, other: Node) -> None:
        self.left = other
        if other is not None:
            other.parent = self

    def set_right(self, other: Node) -> None:
        self.right = other
        if other is not None:
            other.parent = self

    def set_parent(self, parent: Node) -> None:
        if parent is not None:
            if parent.left is self:
                parent.set_left(self)
            else:
                parent.set_right(self)
        else:
            self.parent = None

    def get_size(self) -> int:
        return Node._size(self)

    @staticmethod
    def _size(node: Node) -> int:
        if node is None:
            return 0
        else:
            return Node._size(node.left) + 1 + Node._size(node.right)

    def print_v(self) -> None:
        print(f'^ {self.parent}\n -> {self.right}\n <- {self.left}'
              f'\n color: {self.color}\n value: {self.value}')

    def __repr__(self):
        return self.value

    def __str__(self):
        return f'{self.value}'


class Search_Tree:

    def __init__(self, iterable=None) -> None:
        if iter is None:
            self.tree = []
        else:
            self.tree = list(iterable)
            self.root = None
            for n in self.tree:
                if n.root:
                    self.root = n

    def set_root(self, node: Node) -> None:
        self.root.root = False
        node.root = True
        node.color = Color.BLACK
        self.root = node

    def search(self, value: int) -> Node:
        return self._bin_search(self.root, value)

    def _bin_search(self, root: Node, value: int) -> Node:
        if root.value is None:
            return root

        if root.value == value:
            return root
        elif root.value > value:
            return self._bin_search(root.left, value)
        else:
            return self._bin_search(root.right, value)

    def _make_connection(self, for_delete: Node, node=Node()) -> None:
        # переделать
        if for_delete.parent.left is for_delete:
            for_delete.parent.set_left(node)
        else:
            for_delete.parent.set_right(node)
        self._delete_connections(for_delete)

    def _delete_connections(self, vertex: Node) -> None:
        vertex.set_parent(None)

    def delete(self, value: int) -> None:
        for_delete = self.search(value)
        if for_delete is None:
            raise ValueError('Object doesnt exists')
        else:
            self.tree.remove(for_delete)

            if (for_delete.left.value is None
                    and for_delete.right.value is None):
                if for_delete.root:
                    self.set_root(Node())
                self._make_connection(for_delete)
                return

            elif (for_delete.left.value is not None
                  and for_delete.right.value is None):
                if for_delete.root:
                    self.set_root(for_delete.left)
                    for_delete.left.set_parent(Node())
                else:
                    self._make_connection(for_delete, for_delete.left)
                return

            elif (for_delete.left.value is None
                  and for_delete.right.value is not None):
                if for_delete.root:
                    self.set_root(for_delete.right)
                    for_delete.right.set_parent(Node())
                else:
                    self._make_connection(for_delete, for_delete.right)
                return

            else:
                predecessor = self.predecessor(for_delete)
                if for_delete.root:
                    self.set_root(predecessor)

                fd_l, fd_r, fd_p = (for_delete.left, for_delete.right,
                                    for_delete.parent)
                pr_l, pr_p = predecessor.left, predecessor.parent

                if predecessor is for_delete.left:
                    predecessor.set_parent(fd_p)
                    predecessor.set_left(Node()) # вместо parent
                else:
                    for_delete.set_parent(pr_p)
                    predecessor.set_left(fd_l)
                    predecessor.set_parent(fd_p)

                predecessor.set_right(fd_r)

                for_delete.set_left(pr_l)
                for_delete.set_right(Node())

                self._delete_connections(for_delete)
                return

    def rb_delete(self, value: int) -> None:
        for_delete = self.search(value)
        y_node = for_delete
        y_original_color = for_delete.color
        x_node = None
        if for_delete is None:
            raise ValueError('Object doesnt exists')
        else:
            self.tree.remove(for_delete)

            if (for_delete.left.value is None
                    and for_delete.right.value is None):
                if for_delete.root:
                    self.set_root(Node())
                x_node = Node()
                self._make_connection(for_delete)
                return

            elif (for_delete.left.value is not None
                  and for_delete.right.value is None):
                if for_delete.root:
                    self.set_root(for_delete.left)
                    for_delete.left.set_parent(Node())
                else:
                    x_node = for_delete.left
                    self._make_connection(for_delete, for_delete.left)
                return

            elif (for_delete.left.value is None
                  and for_delete.right.value is not None):
                if for_delete.root:
                    self.set_root(for_delete.right)
                    for_delete.right.set_parent(Node())
                else:
                    x_node = for_delete.right
                    self._make_connection(for_delete, for_delete.right)
                return

            else:
                y_node = self.predecessor(for_delete)
                y_original_color = for_delete.color
                x_node = y_node.left

                if for_delete.root:
                    self.set_root(y_node)

                if y_node is not for_delete.left:
                    self._make_connection(y_node, y_node.right)
                    y_node.set_left(for_delete.left)
                    y_node.left.parent = y_node
                else:
                    x_node.parent = y_node

                self._make_connection(for_delete, y_node) # переставить y на место удаляемой ноды
                y_node.set_right(for_delete.right)
                y_node.right.parent = y_node
                y_node.color = for_delete.color # цвет удаляемой ноды присваивается y

                if y_original_color == Color.BLACK:
                    self.rb_delete_fixup(x_node)
                self._delete_connections(for_delete)
                return

    def rb_delete_fixup(self, node: Node) -> None:
        while node is not self.root and node.color == Color.BLACK:
            if node is node.parent.left:
                brat = node.parent.right

                if brat.color == Color.RED:
                    brat.color = Color.BLACK
                    node.parent.color = Color.RED
                    self._rotate_left(node.parent)
                    brat = node.parent.right

                if (brat.left.color == Color.BLACK
                        and brat.right.color == Color.BLACK):
                    brat.color = Color.RED
                    node = node.parent
                else:
                    if brat.right.color == Color.BLACK:
                        brat.left.color = Color.BLACK
                        brat.color = Color.RED
                        self._rotate_right(brat)
                        brat = node.parent.right
                    brat.color, node.parent.color = node.parent.color, Color.BLACK
                    brat.right.color = Color.BLACK
                    self._rotate_left(node.parent)
                    node = self.root
            else:
                brat = node.parent.left

                if brat.color == Color.RED:
                    brat.color = Color.BLACK
                    node.parent.color = Color.RED
                    self._rotate_right(node.parent)
                    brat = node.parent.left

                if (brat.right.color == Color.BLACK
                        and brat.left.color == Color.BLACK):
                    brat.color = Color.RED
                    node = node.parent
                else:
                    if brat.left.color == Color.BLACK:
                        brat.right.color = Color.BLACK
                        brat.color = Color.RED
                        self._rotate_left(brat)
                        brat = node.parent.left
                    brat.color, node.parent.color = node.parent.color, Color.BLACK
                    brat.left.color = Color.BLACK
                    self._rotate_right(node.parent)
                    node = self.root
        node.color = Color.BLACK

    def select(self, i: int) -> Node:
        return self._select(self.root, i)

    def _select(self, root: Node, i: int) -> Node:
        if root.left.value is None:
            j = 0
        else:
            j = root.left.get_size()

        if i == j + 1:
            return root
        elif i < j + 1:
            return self._select(root.left, i)
        else:
            return self._select(root.right, i - j - 1)

    def insert(self, value: int) -> Node:
        node = self._insert_search(self.root, value)
        node.color = Color.RED
        self._insert_fixup(node)
        return node

    def _insert_fixup(self, node: Node) -> None:
        while node.parent.color == Color.RED:
            if node.parent is node.parent.parent.left: # родительская нода является левым потомком
                uncle = node.parent.parent.right # находим его собрата(дядю)
                if uncle.color == Color.RED:
                    node.parent.color = Color.BLACK
                    uncle.color = Color.BLACK
                    node.parent.parent.color = Color.RED # дед Красный
                    node = node.parent.parent # переопределяем на деда
                else:
                    if node is node.parent.right: # eсли вставленная нода является правым потомком
                        node = node.parent # переопределяем ноду на родителя и делаем ротацию влево
                        self._rotate_left(node) # вставленная нода становится на место родителя \ указатель на родителе
                    node.parent.color = Color.BLACK # меняем цвет вставленной ноды
                    node.parent.parent.color = Color.RED
                    self._rotate_right(node.parent.parent)
            else: # родительская нода является правым потомком
                uncle = node.parent.parent.left # находим его собрата(дядю)
                if uncle.color == Color.RED:
                    node.parent.color = Color.BLACK
                    uncle.color = Color.BLACK
                    node.parent.parent = Color.RED # дед Красный
                    node = node.parent.parent # переопределяем на деда
                else:
                    if node is node.parent.left: # eсли вставленная нода является левым потомком
                        node = node.parent # переопределяем ноду на родителя и делаем ротацию вправо
                        self._rotate_right(node)
                    node.parent.color = Color.BLACK  # меняем цвет вставленной ноды
                    node.parent.parent.color = Color.RED
                    self._rotate_left(node.parent.parent)
        self._root_search(node)
        self.root.color = Color.BLACK # изменить на динамическое вычисление root

    def _insert_search(self, root, value):
        if root.value is None:
            return root

        if root.value == value:
            n = Node(value)
            self.tree.append(n)
            left_child = root.left
            root.set_left(n)
            n.set_left(left_child)
            n.set_right(Node())
            return n

        elif root.value > value:
            node = self._insert_search(root.left, value)
            if node.value is None:
                n = Node(value)
                self.tree.append(n)
                root.set_left(n)
                n.set_left(Node())
                n.set_right(Node())
                return n
            else:
                return node

        else:
            node = self._insert_search(root.right, value)
            if node.value is None:
                n = Node(value)
                self.tree.append(n)
                root.set_right(n)
                n.set_left(Node())
                n.set_right(Node())
                return n
            else:
                return node

    def min(self) -> Node:
        return self._find_min(self.root)

    def _find_min(self, root) -> Node:
        if root.left.value is None:
            return root
        else:
            return self._find_min(root.left)

    def max(self) -> Node:
        return self._find_max(self.root)

    def _find_max(self, root: Node) -> Node:
        if root.right.value is None:
            return root
        else:
            return self._find_max(root.right)

    def predecessor(self, node: Node) -> Node:
        if node.left.value is not None:
            return self._find_max(node.left)
        else:
            return self._up_traverse_right(node)

    def _up_traverse_right(self, node: Node) -> Node:
        if node.parent.value is None:
            return node.parent

        if node.parent.right is node:
            return node.parent
        else:
            return self._up_traverse_right(node.parent)

    def successor(self, node: Node) -> Node:
        if node.right.value is not None:
            return self._find_min(node.right)
        else:
            return self._up_traverse_left(node)

    def _up_traverse_left(self, node: Node) -> Node:
        if node.parent.value is None:
            return node.parent

        if node.parent.left is node:
            return node.parent
        else:
            return self._up_traverse_left(node.parent)

    def output_sorted(self):
        res = []
        return self._output_sorted(self.root, res)

    def _output_sorted(self, root: Node, res: list[Node]) -> list[Node]:
        if root.value is not None:
            res = self._output_sorted(root.left, res)
            res.append(root)
            res = self._output_sorted(root.right, res)
        return res

    def _rotate_left(self, X: Node) -> None:
        """"
        B - Y's left subtree,
        C - Y's right subtree
        """
        if X.right.value is None:
            raise ValueError('Wrong rotation')
        else:
            Y = X.right

        if X.root:
            self.set_root(Y)

        X_parent, B, C = X.parent, Y.left, Y.right

        if X.parent.left is X:
            X.parent.set_left(Y)
        else:
            X.parent.set_right(Y)

        Y.set_left(X)
        Y.set_right(C)
        X.set_right(B)

    def _rotate_right(self, X: Node) -> None:
        """"
        A - X's right subtree,
        B - Y's left subtree,
        C - Y's right subtree
        """
        if X.left.value is None:
            raise ValueError('Wrong rotation')
        else:
            Y = X.left

        if X.root:
            self.set_root(Y)

        X_parent, B, C = X.parent, Y.left, Y.right

        if X.parent.left is X:
            X.parent.set_left(Y)
        else:
            X.parent.set_right(Y)

        X.set_left(C)
        Y.set_right(X)
        Y.set_left(B)

    def _root_search(self, node: Node) -> Node:
        if node.parent.value is None:
            self.set_root(node)
            return node
        else:
            return self._root_search(node.parent)


if __name__ == '__main__':
    n3 = Node(3, root=True)
    n1 = Node(1)
    n2 = Node(2)
    n4 = Node(4)
    n5 = Node(5)

    n3.set_parent(Node())
    n3.set_left(n1)
    n3.set_right(n5)

    n1.set_right(n2)
    n1.set_left(Node())
    n1.color = Color.RED

    n5.set_right(Node())
    n5.set_left(n4)
    n5.color = Color.BLACK

    n4.set_left(Node())
    n4.set_right(Node())
    n4.color = Color.BLACK

    n2.set_left(Node())
    n2.set_right(Node())

    tree = [n1, n5, n2, n3, n4]

    s = Search_Tree(tree)
    # s._rotate_right(n3)
    # n1.print_v()
    # # n2.print_v()
    # n3.print_v()
    # s._rotate_left(n3)
    # n1.print_v()
    # n5.print_v()
    # n3.print_v()
    s._root_search(n3)
    s.insert(6)
    n = s.tree[-1]
    # n.print_v()
    # n1.print_v()

    # n5.print_v()
    s.rb_delete(3)
    s.root.print_v()
    n5.print_v()
    n4.print_v()

