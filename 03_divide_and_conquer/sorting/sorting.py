# Uses python3
import sys
import random

def randomized_quick_sort(a, l, r):
    if l >= r:
        return
    pivot = a[random.randint(l, r)]
    li,ri = l,r
    i = li
    while i <= ri:
        if a[i] < pivot:
            a[li], a[i] = a[i], a[li]
            i += 1
            li += 1
            continue
        if a[i] == pivot:
            i += 1
            continue
        if a[i] > pivot:
            a[ri], a[i] = a[i], a[ri]
            ri -= 1
            continue
    
    randomized_quick_sort(a, l, li - 1)
    randomized_quick_sort(a, ri + 1, r)

input = sys.stdin.read()
n, *a = list(map(int, input.split()))
randomized_quick_sort(a, 0, n - 1)
for x in a:
    print(x, end=' ')
