#Uses python3
import sys
import math
import random
import time

def d(p1,p2):
    x1, y1 = p1
    x2, y2 = p2
    return math.sqrt( (x1 - x2) ** 2 + (y1 - y2) ** 2 )

def minimum_distance_naive(points):
    if len(points) <= 1:
        return 0.0
    min_d = sys.maxsize
    l = len(points)
    for i in range(0, l):
        for j in range(i + 1, l):
            x = points[i]
            y = points[j]
            min_d = min(min_d, d(x,y))
    return min_d

def minimum_distance_r(points, l, r):
    if l >= r:
        return sys.maxsize

    if r - l == 1:
        return d(points[l], points[r])
    split_x = (points[l][0] + points[r][0]) / 2

    m = l
    for i in range(l, r + 1):
        if points[i][0] >= split_x:
            break
        m = i

    min_d_left = minimum_distance_r(points, l, m)
    min_d_right = minimum_distance_r(points, m + 1, r)

    min_d = min(min_d_left, min_d_right)

    for i in range(l, m + 1):
        if split_x - points[i][0] > min_d:
            continue
        for j in range(m + 1, r + 1):
            if points[j][0] - split_x > min_d:
                continue
            min_d = min(min_d, d(points[i], points[j]))
    return min_d

def minimum_distance(points):
    if len(points) <= 1:
        return 0.0
    points.sort(key=lambda x: x[0])
    return minimum_distance_r(points, 0, len(points) - 1)

test = False

def generate_test_case(size):
    points = [0] * size
    min_coordinate = -10**9
    max_coordinate =  10**9

    for i in range(0, size):
        x = 0#random.randint(min_coordinate, max_coordinate)
        y = random.randint(min_coordinate, max_coordinate)
        points[i] = (x,y)
    return points

if test:
    times = []
    test_case_count = 500000
    
    success = 0
    failures = []

    i = 0
    for i in range(0, test_case_count):        
        test_case_size = 1000
        points = generate_test_case(test_case_size)
        # print("running against " + str(len(points)) + " points")
        expected = minimum_distance_naive(points)
        start = time.time()
        actual = minimum_distance(points)         
        end = time.time()
        times.append(end - start)
        print (str(expected) + " - " + str(actual))
        if actual != expected:
            failures.append((points, expected, actual))
            raise Exception("Failed. Input: {0}, Expected: {1}, Actual: {2}".format(points, expected, actual))
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
        print("points | expected | actual")
        for points,expected,actual in failures:
            print("%s | %s | %s" % (points,expected,actual))
    print("Total time: " + str(sum(times)))
else:
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    x = data[1::2]
    y = data[2::2]
    points = []
    for i in range(0, len(x)):
        points.append((x[i], y[i]))
    # points.sort(k)
    min_d = 0 if len(points) <= 1 else minimum_distance(points)
    print("{0:.9f}".format(min_d))
