# Uses python3
import sys

def get_sort_key(x):
    return x[0]

def combine(left, right):
    r = { }
    for x, count in (left + right):
        if x in r:
            r[x] += count
        else:
            r[x] = count
    return list(r.items())

def get_majority_element_internal(a, left, right):
    if left > right:
        return []
    if left == right:
        return [(a[left], 1)]
    if left + 1 == right:
        if a[left] == a[right]:
            return [(a[left], 2)]
        else:
            return [(a[left], 1), (a[right], 1)]

    mid = (left + right) // 2
    left_results = get_majority_element_internal(a, left, mid)
    right_results = get_majority_element_internal(a, mid + 1, right)
    return combine(left_results, right_results)

def get_majority_element(a, left, right):
    counts = get_majority_element_internal(a, left, right)
    if len(counts) == 0:
        return -1

    counts.sort(key=lambda x:x[1],reverse=True)
    _, top_count = counts[0]
    return 1 if top_count > len(a) // 2 else -1

input = sys.stdin.read()
n, *a = list(map(int, input.split()))
if get_majority_element(a, 0, n-1) != -1:
    print(1)
else:
    print(0)
