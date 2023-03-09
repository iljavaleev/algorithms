from __future__ import annotations
from typing import Generic, TypeVar, Optional
from enum import Enum

T = TypeVar('T')


class Color(Enum):
    BLACK = 1
    RED = 2


class BinaryTreeNode(Generic[T]):

    def __init__(self, value: T, color: Color = Color.RED) -> None:
        self.left: Optional[BinaryTreeNode] = None
        self.right: Optional[BinaryTreeNode] = None
        self.parent: Optional[BinaryTreeNode] = None
        self.color = color
        self.value = value

    def is_leaf(self) -> bool:
        return self.left is None and self.right is None

    def __str__(self) -> str:
        return f'value: {self.value}'

    def __repr__(self) -> str:
        return f'value: {self.value}'

    def set_left(self, other: BinaryTreeNode[T]) -> None:
        self.left = other
        other.parent = self

    def set_right(self, other: BinaryTreeNode) -> None:
        self.right = other
        other.parent = self

    def set_parent(self, parent: BinaryTreeNode) -> None:
        if parent.value is not None:
            if parent.left is self:
                parent.set_left(self)
            else:
                parent.set_right(self)
        else:
            self.parent = SENTINEL


SENTINEL = BinaryTreeNode(None, Color.BLACK)
ROOT = None

def print_value(node: BinaryTreeNode) -> None:
    print(f"BinaryTreeNode [item={node.value}, left={node.left}, right={node.right}, parent={node.parent}]")


def find(current: BinaryTreeNode, search_for: T) -> BinaryTreeNode | None:
    while current.value is not None and current.value != search_for:

        if current.value > search_for:
            current = current.left
        else:
            current = current.right

    return current


def get_max(current: BinaryTreeNode) -> BinaryTreeNode | None:
    while current.right.value is not None:
        current = current.right

    return current


def get_min(current: BinaryTreeNode) -> BinaryTreeNode | None:
    while current.left.value is not None:
        current = current.left
    return current


def successor(current: BinaryTreeNode) -> BinaryTreeNode | None:
    if current.right is not SENTINEL:
        return get_min(current.right)
    else:
        parent = current.parent
        while parent is not SENTINEL and parent.right == current:
            current = parent
            parent = parent.parent
    return parent


def predecessor(current: BinaryTreeNode) -> BinaryTreeNode | None:
    if current.left is not SENTINEL:
        return get_max(current.left)
    else:
        parent = current.parent
        while parent is not SENTINEL and parent.left == current:
            current = parent
            parent = parent.parent
    return parent


def insert_fixup(node: BinaryTreeNode) -> None:
    """node is RED."""
    global ROOT
    while node.parent.color is Color.RED:
        if node.parent.parent.left is node.parent:
            uncle = node.parent.parent.right
            if uncle.color is Color.RED:
                node.parent.color = Color.BLACK
                uncle.color = Color.BLACK
                node.parent.parent.color = Color.RED
                node = node.parent.parent
            else:
                if node.parent.right is node:
                    node = node.parent
                    left_rotate(node)
                node.parent.color = Color.BLACK
                node.parent.parent.color = Color.RED
                right_rotate(node.parent.parent)
        else:
            uncle = node.parent.parent.left
            if uncle.color is Color.RED:
                node.parent.color = Color.BLACK
                uncle.color = Color.BLACK
                node.parent.parent.color = Color.RED
                node = node.parent.parent
            else:
                if node.parent.left is node:
                    node = node.parent
                    right_rotate(node)
                node.parent.color = Color.BLACK
                node.parent.parent.color = Color.RED
                left_rotate(node.parent.parent)
    ROOT.color = Color.BLACK


def insert(to_add: BinaryTreeNode) -> None:
    global ROOT
    current = ROOT
    parent = SENTINEL
    while current is not SENTINEL:
        parent = current
        if current.value > to_add.value:
            current = current.left
        else:
            current = current.right
    to_add.parent = parent
    if parent is SENTINEL:
        ROOT = to_add
    elif parent.value > to_add.value:
        parent.left = to_add
    else:
        parent.right = to_add
    to_add.left = SENTINEL
    to_add.right = SENTINEL
    to_add.color = Color.RED
    insert_fixup(to_add)


def delete(to_delete: BinaryTreeNode) -> None:
    next = to_delete
    next_original_color = next.color

    if to_delete.left is SENTINEL:
        to_fix = to_delete.right
        transplant(to_delete, to_delete.right)
    elif to_delete.right is SENTINEL:
        to_fix = to_delete.left
        transplant(to_delete, to_delete.left)
    else:
        next = successor(to_delete)
        next_original_color = next.color
        to_fix = next.right

        if to_delete.right is not next:
            transplant(next, next.right)
            next.right = to_delete.right
            next.right.parent = next
        transplant(to_delete, next)
        next.left = to_delete.left
        next.left.parent = next
        next.color = to_delete.color

    if next_original_color is Color.BLACK: # fixup только если черный цвет у ноды next
        delete_fixup(to_fix)


def delete_fixup(node: BinaryTreeNode) -> None:
    while node is not ROOT and node.color == Color.BLACK:
        if node is node.parent.left:
            brat = node.parent.right

            if brat.color == Color.RED:
                brat.color = Color.BLACK
                node.parent.color = Color.RED
                left_rotate(node.parent)
                brat = node.parent.right

            if (brat.left.color == Color.BLACK
                    and brat.right.color == Color.BLACK):
                brat.color = Color.RED
                node = node.parent
            else:
                if brat.right.color == Color.BLACK:
                    brat.left.color = Color.BLACK
                    brat.color = Color.RED
                    right_rotate(brat)
                    brat = node.parent.right
                brat.color, node.parent.color = node.parent.color, Color.BLACK
                brat.right.color = Color.BLACK
                left_rotate(node.parent)
                node = ROOT
        else:
            brat = node.parent.left

            if brat.color == Color.RED:
                brat.color = Color.BLACK
                node.parent.color = Color.RED
                right_rotate(node.parent)
                brat = node.parent.left

            if (brat.right.color == Color.BLACK
                    and brat.left.color == Color.BLACK):
                brat.color = Color.RED
                node = node.parent
            else:
                if brat.left.color == Color.BLACK:
                    brat.right.color = Color.BLACK
                    brat.color = Color.RED
                    left_rotate(brat)
                    brat = node.parent.left
                brat.color, node.parent.color = node.parent.color, Color.BLACK
                brat.left.color = Color.BLACK
                right_rotate(node.parent)
                node = ROOT
    node.color = Color.BLACK


def transplant(u_node: BinaryTreeNode, v_node: BinaryTreeNode) -> None:
    """Меняет parnet связи."""
    global ROOT

    if u_node.parent is SENTINEL:
        ROOT = v_node
    elif u_node.parent.left is u_node:
        u_node.parent.left = v_node
    else:
        u_node.parent.right = v_node

    v_node.parent = u_node.parent


def pre_order(root: BinaryTreeNode) -> None:
    if root is SENTINEL:
        return
    print(root.value)
    pre_order(root.left)
    pre_order(root.right)


def inorder(root: BinaryTreeNode) -> None:
    if root is SENTINEL:
        return
    inorder(root.left)
    print(root.value)
    inorder(root.right)


def post_order(root: BinaryTreeNode) -> None:
    if root is not SENTINEL:
        post_order(root.left)
        post_order(root.right)
        print(root.value)


def left_rotate(root: BinaryTreeNode) -> None:
    global ROOT
    next_root = root.left
    root.right = next_root.left

    if next_root.left is not SENTINEL:
        root.right.parent = root
    next_root.parent = root.parent
    if root.parent is SENTINEL:
        ROOT = next_root
    elif root.parent.left is root:
        root.parent.left = next_root
    else:
        root.parent.right = next_root

    next_root.left = root
    root.parent = next_root


def right_rotate(root: BinaryTreeNode) -> None:
    global ROOT
    next_root = root.right
    root.left = next_root.right

    if next_root.right is not SENTINEL:
        root.left.parent = root
    next_root.parent = root.parent
    if root.parent is SENTINEL:
        ROOT = next_root
    elif root.parent.left is root:
        root.parent.left = next_root
    else:
        root.parent.right = next_root

    next_root.right = root
    root.parent = next_root


def is_leaf(node: BinaryTreeNode) -> None:
    node.left = SENTINEL
    node.right = SENTINEL


if __name__ == '__main__':

    _7 = BinaryTreeNode(7, Color.BLACK)
    ROOT = _7
    _7.parent = SENTINEL

    _2 = BinaryTreeNode(2, Color.RED)
    _7.left = _2
    _2.parent = _7

    _11 = BinaryTreeNode(11, Color.RED)
    _7.right = _11
    _11.parent = _7

    _1 = BinaryTreeNode(1, Color.BLACK)
    _2.left = _1
    _1.parent = _2
    is_leaf(_1)

    _5 = BinaryTreeNode(5, Color.BLACK)
    _2.right = _5
    _5.parent = _2
    _5.right = SENTINEL

    _4 = BinaryTreeNode(4, Color.RED)
    _5.left = _4
    _4.parent = _5
    is_leaf(_4)

    _8 = BinaryTreeNode(8, Color.BLACK)
    _11.left = _8
    _8.parent = _11
    is_leaf(_8)

    _14 = BinaryTreeNode(14, Color.BLACK)
    _11.right = _14
    _14.parent = _11
    _14.left = SENTINEL

    _15 = BinaryTreeNode(15, Color.RED)
    _14.right = _15
    _15.parent = _14
    is_leaf(_15)

    # insert(BinaryTreeNode(1))
    # insert(BinaryTreeNode(2))
    # insert(BinaryTreeNode(4))
    #
    # n = find(current=_3, search_for=1)
    # # print(get_min(_3))
    # print(successor(n))
    # print(predecessor(n))
    pre_order(ROOT)
    print()
    post_order(ROOT)
    print()
    inorder(ROOT)
