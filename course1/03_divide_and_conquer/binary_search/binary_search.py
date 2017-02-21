# Uses python3
import sys

def binary_search(a, x):
    left, right = 0, len(a)-1

    while left <= right:
        mid_index = (right + left) // 2
        mid = a[mid_index]
        if x == mid:
            return mid_index
        if x < mid:
            right = mid_index - 1
        else:
            left = mid_index + 1

    return -1

def linear_search(a, x):
    for i in range(len(a)):
        if a[i] == x:
            return i
    return -1

input = sys.stdin.read()
data = list(map(int, input.split()))
n = data[0]
m = data[n + 1]
a = data[1 : n + 1]
for x in data[n + 2:]:
    print(binary_search(a, x), end = ' ')
