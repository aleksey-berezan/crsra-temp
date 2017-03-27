# python3

import sys, threading

sys.setrecursionlimit(10 ** 6)  # max depth of recursion
threading.stack_size(2 ** 27)  # new thread will get stack of such size


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
        self.trees[0].traverse_preorder(action=lambda data: result.append(data))
        return result

    def postOrder(self):
        result = []
        self.trees[0].traverse_postorder(action=lambda data: result.append(data))
        return result


def main():
    tree = TreeOrders()
    tree.read()
    print(" ".join(str(x) for x in tree.inOrder()))
    print(" ".join(str(x) for x in tree.preOrder()))
    print(" ".join(str(x) for x in tree.postOrder()))


threading.Thread(target=main).start()
