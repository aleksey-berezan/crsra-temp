# Uses python3
import sys
from collections import namedtuple
from itertools import permutations

s = namedtuple('s', 'start end')

def optimal_points(segments):
    def segment_len(s):
        left,right = s
        return right - left
    def intersect(a, b):
        la,ra = a
        lb,rb = b

        if la < lb and ra < lb:
            return False
        if la > rb and ra > rb:
            return False
        return True

    points = []
    
    while len(segments) > 0:
        # segments.sort(key=lambda x:x[0])
        min_s = segments[0]
        for s in segments:
            min_s = min_s if segment_len(min_s) < segment_len(s) else s

        intersected = [min_s]
        for s in segments:
            if s is min_s:
                continue

            flag = True
            for x in intersected:
                if not intersect(x, s):
                    flag = False
                    break
            if flag:
                intersected.append(s)

        # intersected = [x for x in segments if intersect(x, min_s)]

        max_left = 0
        min_right = sys.maxsize

        for (left, right) in intersected:
            (max_left, min_right) = (max([max_left, left]),min([min_right,right]))

        for x in intersected:             
            segments.remove(x)
        points.append(min_right)
    return points

test = True
if test:
    test_cases = [
        # ([(1,1),(2,2),(3,3)],[1,2,3]),
        # ([(1,3),(2,5),(3,6)],[3]),
        # ([(4,7),(1,3),(2,5),(5,6)],[3,5]),
        # ([(1,2),(3,4),(5,6),(7,8)],[2,4,6,8]),
        # ([(1,1)],[1]),
        # ([(1,1),(1,1)],[1]),
        # ([(1,2),(2,3),(3,4)],[2,3]),
        # ([(1,2),(2,3),(3,4),(5,6)],[2,3,6]),
        # ([(1,2),(2,3),(3,4),(5,6),(5,5)],[2,3,5]),
        # ([(1, 2), (2, 3), (3, 4), (5, 6), (5, 5)],[2,3,5]),        
        # ([(2, 5), (1, 3), (4, 6)],[3,5]),        
        # ([(2, 5), (1, 3), (4, 6),(5,7)],[3,5]),        
        # ([(2, 5), (1, 3), (4, 6),(5,7),(5,8)],[3,5]),        
        # ([(2, 5), (1, 3), (4, 6),(5,7),(5,8),(8,9),(9,10)],[3,5,9]),
        # ([(2, 5), (1, 3), (4, 6),(5,7),(6,8),(8,9),(9,10)],[3,6,9]),
        ([(9, 10), (8, 9), (5, 7), (1, 3), (2, 5), (6, 8), (4, 6)],[3,6,9]),
        # ([(2, 5), (1, 3), (4, 6),(5,5),(6,8),(8,9),(9,10)],[3,5,8,9]),
        # ([(5,5),(6,8),(8,9),(9,10), (100,200), (12, 300)],[5,8,9,200]),
        # ([(1,3),(6,8),(8,9),(9,10), (100,200), (12, 300)],[3,8,9,200]),
        # ([(12, 300), (100, 200), (9, 10), (8, 9), (6, 8), (1, 3)],[3,8,9,200]),
    ]

    success = 0
    failures = []

    for input, expected in test_cases:
        for input2 in [input]:#permutations(input):
            actual = optimal_points(list(input2))
            actual.sort()
            expected.sort()
            if len(actual) == len(expected):
                success += 1
            else:
                failures.append((input2, expected, actual))

    failed = len(failures)
    print("Success: {0}, Failed: {1}".format(success, failed))
    print("")
    if failed == 0:
        print("Success")
    else:
        print("FAILED!!!")
        print("Failed Test Cases:")
        print("Input - Expected - Actual")
        for input, expected, actual in failures:
            print("%s - %s - %s" % (input, expected, actual))
else:
    # main
    lines = sys.stdin.readlines()
    input = '\n'.join(lines)
    n, *data = map(int, input.split())
    ss = list(map(lambda x: s(x[0], x[1]), zip(data[::2], data[1::2])))
    points = optimal_points(ss)
    print(len(points))
    for p in points:
        print(p, end=' ')
