# python3

import sys
import threading

sys.setrecursionlimit(10 ** 6)  # max depth of recursion
threading.stack_size(2 ** 27)  # new thread will get stack of such size


def select_non_none(values, selection_func):
    m = None
    for v in values:
        if v == None:
            continue
        if m == None:
            m = v
            continue
        m = selection_func(v, m)
    return m


def select_max(values):
    return select_non_none(values, selection_func=max)


def select_min(values):
    return select_non_none(values, selection_func=min)


class TreeNode:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def traverse_inorder(self, action):
        if self.left != None:
            self.left.traverse_inorder(action)

        action(self.data)

        if self.right != None:
            self.right.traverse_inorder(action)

    def traverse_preorder(self, action):
        action(self.data)

        if self.left != None:
            self.left.traverse_preorder(action)

        if self.right != None:
            self.right.traverse_preorder(action)

    def traverse_postorder(self, action):
        if self.left != None:
            self.left.traverse_postorder(action)

        if self.right != None:
            self.right.traverse_postorder(action)

        action(self.data)

    def is_bst(self):
        min_right = None
        max_left = None
        min_right2 = None
        max_left2 = None

        if self.left != None:
            if not (self.left.data < self.data):
                return (False, None, None)
            left_isbst, max_left, min_right = self.left.is_bst()
            if not left_isbst:
                return (False, None, None)
            if max_left != None and not (max_left < self.data):
                return (False, None, None)

        if self.right != None:
            if not (self.right.data > self.data):
                return (False, None, None)
            right_isbst, max_left2, min_right2 = self.right.is_bst()
            if not right_isbst:
                return (False, None, None)
            if min_right2 != None and not (min_right2 > self.data):
                return (False, None, None)

        return (True,
                select_max([self.data, max_left, max_left2]),
                select_min([self.data, min_right, min_right2]))


class TreeOrders:
    def read(self):
        self.n = int(sys.stdin.readline())
        self.key = [0 for i in range(self.n)]
        self.left = [0 for i in range(self.n)]
        self.right = [0 for i in range(self.n)]
        self.trees = [TreeNode(None) for x in range(0, self.n)]
        for i in range(self.n):
            [d, l, r] = map(int, sys.stdin.readline().split())
            self.trees[i].data = d
            self.trees[i].left = self.trees[l] if l != -1 else None
            self.trees[i].right = self.trees[r] if r != -1 else None
            # self.key[i] = a
            # self.left[i] = b
            # self.right[i] = c

    def inOrder(self):
        result = []
        self.trees[0].traverse_inorder(action=lambda data: result.append(data))
        return result

    def preOrder(self):
        result = []
        self.trees[0].traverse_preorder(
            action=lambda data: result.append(data))
        return result

    def postOrder(self):
        result = []
        self.trees[0].traverse_postorder(
            action=lambda data: result.append(data))
        return result

    def is_bst(self):
        if len(self.trees) == 0:
            return True
        (r, l, r) = self.trees[0].is_bst()
        return r


def main():
    tree = TreeOrders()
    tree.read()

    if tree.is_bst():
        print("CORRECT")
    else:
        print("INCORRECT")


threading.Thread(target=main).start()
