# Uses python3
import sys
import random
import time

def binary_search(a, x, lean_left, left, right):
    #left, right = 0, len(a)-1

    while left <= right:
        mid_index = (right + left) // 2
        mid = a[mid_index]
        if x == mid:
            inc = -1 if lean_left else +1
            while (mid_index >= 0 and mid_index < len(a)) and x == a[mid_index]:
                mid_index += inc
            return mid_index - inc
        if x < mid:
            right = mid_index - 1
        else:
            left = mid_index + 1

    return max(-1, min(right if lean_left else left, len(a) - 1))

def fast_count_segments_internal(segments, points):
    sorted_points = list(points)
    sorted_points.sort()
    indexed_points = [(points[i], i) for i in range(0, len(points))]
    indexed_points.sort(key=lambda x: x[0])
    counts = [0] * len(points)

    for s in segments:
        s_left, s_right = s
        left_index = binary_search(sorted_points, s_left, True, 0, len(sorted_points)-1)
        right_index = binary_search(sorted_points, s_right, False, left_index,len(sorted_points)-1)

        for i in range(left_index, right_index + 1):
            p = sorted_points[i]
            if s_left <= p <= s_right:
                p,pi = indexed_points[i]
                # indexed_points[i] = (p,pi,cnt+1)
                counts[pi] += 1
    
    
    # for (p,i,cnt) in indexed_points:
    #     counts[i] = cnt
    return counts

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

def fst(tuple): return tuple[0]

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

    # segments = [(starts[i], ends[i]) for i in range(0, len(starts))]
    # return fast_count_segments_internal(segments, points)

def naive_count_segments(starts, ends, points):
    cnt = [0] * len(points)
    for i in range(len(points)):
        for j in range(len(starts)):
            if starts[j] <= points[i] <= ends[j]:
                cnt[i] += 1
    return cnt

test = False

def generate_segment(min_value, max_value):
    l = random.randint(min_value, max_value)
    r = random.randint(min_value, max_value)
    while r == l:
        r = random.randint(min_value, max_value)
    return (min(l,r), max(l,r))

def generate_test_case(segments_count, points_count):
    starts = []
    ends = []
    points = []
    
    min_value = 0
    max_value = 9

    for i in range(0, segments_count):
        s = generate_segment(min_value, max_value)        
        starts.append(s[0])
        ends.append(s[1])
    for i in range(0,points_count):         
        points.append(random.randint(min_value, max_value))

    return (starts, ends, points)

if test:
    times = []
    test_case_count = 10
    
    success = 0
    failures = []

    test_cases = [
        ([2], [4],[4]),
        ([-4], [2], [-4, -4, 2, 10, -4]),
        ([8, 9, 12], [11, 11, 14], [11, 11, 12])
    ]

    i = 0
    for i in range(0, test_case_count):        
        segments_count = 20000
        points_count = 500
        # (starts, ends, points) = test_cases[i]# ([2], [4],[4])
        # (starts, ends, points) = ([2, 8, 6, 6, 1, 4, 3, 3, 7, 0],[3, 2, 7, 5, 7, 0, 6, 5, 0, 8],[2, 2, 8, 7, 8])#[3, 3, 1, 3, 1]
        (starts, ends, points) = generate_test_case(segments_count, points_count)
        
        # print("running against " + str(len(points)) + " points")
        expected = naive_count_segments(starts, ends, points)
        start = time.time()
        actual = fast_count_segments(starts, ends, points)         
        end = time.time()
        times.append(end - start)
        # print (str(expected) + " - " + str(actual))
        if actual != expected:
            failures.append((starts, ends, points, expected, actual))
            # raise Exception("Failed. Starts: {0}, Ends: {1}, Points: {2}, Expected: {3}, Actual: {4}".format(starts, ends, points, expected, actual))
        else:
            success += 1
        i += 1
        if i % 50 == 0:
            print(str(i) + " cases so far")

    failed = len(failures)
    print("Success: {0}, Failed: {1}".format(success, failed))
    print("")
    if failed == 0:
        print("Success")
    else:
        print("FAILED!!!")
        print("Failed Test Cases:")
        print("starts | ends | points | expected | actual")
        for starts, ends, points, expected, actual in failures:
            print("{0},{1},{2} | {3} | {4}".format(starts, ends, points, expected, actual))
    print("Total time: " + str(sum(times)))
else:
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
