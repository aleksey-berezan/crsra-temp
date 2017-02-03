# Uses python3
import sys
import random

def compare(left_point, right_point):
    (left_value, left_type, left_index) = left_point
    (right_value, right_type, right_index) = right_point
    d = left_value - right_value
    if d != 0:
        return d
    
    order = ['l', 'p', 'r']
    left_order = order.index(left_type)
    right_order = order.index(right_type)
    return left_order - right_order

def sort_points(all_points, l, r):
    if l >= r:
        return

    pivot = all_points[random.randint(l, r)]
    lo, hi = l, r
    i = l
    while i <= hi:
        c = compare(all_points[i], pivot)
        if c < 0:
            all_points[i], all_points[lo] = all_points[lo], all_points[i]
            i += 1
            lo += 1
            continue
        if c == 0:
            i += 1
            continue
        if c > 0:
            all_points[hi], all_points[i] = all_points[i], all_points[hi]
            hi -= 1
            continue
        raise Exception("Unknown error")
    
    sort_points(all_points, l, lo - 1)
    sort_points(all_points, hi + 1, r)

def fast_count_segments(starts, ends, points):
    all_points = [(0,'0',0)] * (len(starts) + len(ends) + len(points))# value, char, index

    offset = 0
    for i in range(0, len(starts)):
        all_points[offset + i] = (starts[i], 'l', -1)
    offset += len(starts)
    for i in range(0, len(ends)):
        all_points[offset + i] = (ends[i], 'r', -1)
    offset += len(ends)
    for i in range(0, len(points)):
        all_points[offset + i] = (points[i], 'p', i)
    
    sort_points(all_points, 0, len(all_points) - 1)
    counts = [0] * len(points)
    counter = 0

    for (value, type, index) in all_points:
        if type == 'l':
            counter += 1
        elif type == 'r':
            counter -= 1
        elif type == 'p':
            counts[index] = counter
        else:
            raise Exception("Unexpected type " + str(type))
    return counts

input = sys.stdin.read()
data = list(map(int, input.split()))
n = data[0]
m = data[1]
starts = data[2:2 * n + 2:2]
ends   = data[3:2 * n + 2:2]
points = data[2 * n + 2:]
#use fast_count_segments
cnt = fast_count_segments(starts, ends, points)
for x in cnt:
    print(x, end=' ')
