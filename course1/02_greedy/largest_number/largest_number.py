#Uses python3

import sys
import itertools

def is_greater(left, right):
    if left == right:
        return True

    (ls, rs) = (str(left), str(right))
    return int(ls + rs) >= int(rs + ls)

def largest_number(a):
    if len(a) == 0:
        return "0"

    a = [str(x) for x in a]

    res = ""
    while len(a) > 0:
        max_digit = "0"
        for d in a:
            if is_greater(d, max_digit):
                max_digit = d
        res += str(max_digit)
        a.remove(max_digit)

    return str(int(res))

lines = sys.stdin.readlines()
input = '\n'.join(lines)

data = input.split()
a = data[1:]
print(largest_number(a))