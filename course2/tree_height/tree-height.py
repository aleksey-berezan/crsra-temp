# python3

import sys, threading
sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

class TreeNode:
        def __init__(self, value):
                self.value = value
                self.children = []
                self.parent = None

        def get_height(self, current_height = 0):
                if len(self.children) == 0:
                        return current_height + 1
                else:
                        l = max(map(lambda c: c.get_height(current_height + 1), self.children))
                        return l

def read_nodes(s):
        items = list(map(lambda x: int(x), s.split()))
        nodes = [None] * len(items)
        for i in range(0, len(items)):
                nodes[i] = TreeNode(i)
        for i in range(0, len(items)):
                parent_index = items[i]
                if(parent_index > -1):
                        parent = nodes[parent_index]
                        parent.children.append(nodes[i])
                        nodes[i].parent = parent
        return nodes

def main():
        ignored = input()
        s = input()
        nodes = read_nodes(s)
        root_node = [n for n in nodes if n.parent == None][0]
        height = root_node.get_height(0)
        print(height)

threading.Thread(target=main).start()
