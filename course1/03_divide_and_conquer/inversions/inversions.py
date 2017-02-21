# Uses python3
import sys

def split(array):
    m = len(array) // 2
    return (array[:m], array[m:])

def merge(left, right, inversions_acc):
    # print("Merging {0} - {1}. Inversions in: {2}".format(left, right, inversions_acc))
    result = [0] * (len(left) + len(right))
    l, r = 0, 0
    inversions = 0
    for i in range(0, len(result)):
        if l >= len(left):
            result[i] = right[r]
            r += 1
            continue
        if r >= len(right):
            result[i] = left[l]
            l += 1
            continue
        if left[l] <= right[r]:
            result[i] = left[l]
            l += 1
        else:
            result[i] = right[r]
            r += 1
            inversions += (len(left) - l)
    inversions_acc += inversions
    # print("Inversions added: {0}, Inversions out: {1}".format(inversions, inversions_acc))
    return result, inversions_acc

def merge_sort(array):
    if len(array) <= 1:
        return (array, 0)

    left, right = split(array)
    (left_sorted, li) = merge_sort(left)
    (right_sorted, ri) = merge_sort(right)
    return merge(left_sorted, right_sorted, li + ri)

input = sys.stdin.read()
n, *a = list(map(int, input.split()))
(sorted, inversions) = merge_sort(a)
print(inversions)
