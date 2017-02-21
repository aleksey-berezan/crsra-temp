#Uses python3

import sys

def max_dot_product(a, b):
    #write your code here
    res = 0
    a.sort()
    b.sort()
    for i in range(len(a)):
        res += a[i] * b[i]
    return res

# main
lines = sys.stdin.readlines()
input = '\n'.join(lines)
data = list(map(int, input.split()))
n = data[0]
a = data[1:(n + 1)]
b = data[(n + 1):]
print(max_dot_product(a, b))
