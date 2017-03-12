# python3

import sys

def get_parent(parents, index):
    traversed = []
    current = index
    while parents[current] != None:
        traversed.append(current)
        current = parents[current]

    for t in traversed:
        parents[t] = current
    return current

def merge(parents, rows, destination, source):
    real_destination = get_parent(parents, destination)
    real_source = get_parent(parents, source)

    if real_destination == real_source:
        return -1
    else:
        rows[real_destination] += rows[real_source]
        parents[real_source] = real_destination
        rows[real_source] = 0
        return rows[real_destination]

# main
n, m = map(int, sys.stdin.readline().split())
rows = list(map(int, sys.stdin.readline().split()))
parents = [None] * n
ans = []
last = max(rows)
operations = []
ops = [(3, 5),(2, 4),(1, 4),(5, 4),(5, 3)]
for i in range(m):
    destination, source = map(int, sys.stdin.readline().split())
    operations.append((destination - 1, source - 1))

last = max(rows)
for destination, source in operations:
    l = merge(parents, rows, destination, source)
    if l != -1:
        last = max(l, last)

    ans.append(last)

for a in ans:
    print(a)