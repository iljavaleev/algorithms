from binaryTreeNode import *
from typing import Callable, Any, Sequence


def it_preorder(node: BinaryTreeNode,
                action: Callable,
                container: Sequence = None) -> Any:
    stack = [node]
    while stack:
        node = stack.pop()
        if node is not SENTINEL:
            action(node)
            stack.append(node.right)
            stack.append(node.left)


def it_postorder(node: BinaryTreeNode, action: Callable) -> Any:
    last_deleted = None
    stack = []
    while stack or node is not SENTINEL:
        if node is not SENTINEL:
            stack.append(node)
            node = node.left
        else:
            peek_node = stack[-1]
            if (peek_node.right is not SENTINEL
                    and peek_node.right is not last_deleted):
                node = peek_node.right
            else:
                last_deleted = stack.pop()
                action(last_deleted.value)


def it_in_order(node: BinaryTreeNode,
                action: Callable,
                container: Callable = None) -> Any:
    stack = []
    while True:
        if node is not SENTINEL:
            stack.append(node)
            node = node.left
        elif stack:
            node = stack.pop()
            print(node)
            node = node.right
        else:
            return


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

    # pre_order(ROOT)
    # print()
    post_order(ROOT)
    # print()

    # inorder(ROOT)
    print()
    # it_preorder(ROOT, print)
    it_postorder(ROOT, print)
    # it_in_order(ROOT, print)
