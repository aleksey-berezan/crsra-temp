# python3

import sys

class Stack:
    def __init__(self):
        self.items = []

    def count(self):
        return len(self.items)

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.count() == 0:
            raise Exception("Stack is empty")
        r = self.items[self.count() - 1]
        del self.items[-1]
        return r

#main
text = input()

stack = Stack()
open_braces = list("([{")
close_braces = list(")]}")

success = True
for i, next in enumerate(text):
    if next in open_braces:
        stack.push((next,i))
        continue
    if next in close_braces:
        if stack.count() == 0:
            print(i + 1)
            success = False
            break
        index = close_braces.index(next)
        expected = open_braces[index]
        actual = stack.pop()[0]
        if actual != expected:
            print(i + 1)
            success = False
            break

if success and stack.count() > 0:
    error_index = stack.pop()[1]
    print(error_index + 1)
    success = False

if success:
    print("Success")