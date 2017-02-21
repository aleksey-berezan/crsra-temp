# Uses python3
import sys
from collections import namedtuple
from itertools import permutations

s = namedtuple('s', 'start end')

def optimal_points(segments):
    points = []
    while len(segments) > 0:
        segments.sort(key=lambda x:x[0])
        
        min_left,min_right = segments[0]
        intersected = [segments[0]]
        for segment in segments[1:]:
            left,right = segment
            if left <= min_right:
                intersected.append(segment)
                min_right = min(min_right,right)
            else:
                break
        points.append(min_right)
        for segment in intersected:
            segments.remove(segment)
    return points

# main
lines = sys.stdin.readlines()
input = '\n'.join(lines)
n, *data = map(int, input.split())
ss = list(map(lambda x: s(x[0], x[1]), zip(data[::2], data[1::2])))
points = optimal_points(ss)
print(len(points))
for p in points:
    print(p, end=' ')
