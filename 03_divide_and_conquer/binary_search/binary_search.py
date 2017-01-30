# Uses python3
import sys
import random

def binary_search(a, x):
    left, right = 0, len(a)-1

    while left <= right:
        mid_index = (right + left) // 2
        mid = a[mid_index]
        if x == mid:
            return mid_index
        if x < mid:
            right = mid_index - 1
        else:
            left = mid_index + 1

    return -1

def linear_search(a, x):
    for i in range(len(a)):
        if a[i] == x:
            return i
    return -1

test = False

def generate_test_case(size):
    # size = 5
    min_num = 0
    max_num = 9999
    a = [0] * size
    for i in range(0, size):
        a[i] = random.randint(min_num,max_num)
    a.sort()
    
    index = random.randint(0, size * 2)
    if index >= 0 and index < size:
        x = a[index]
    else:
        x = max_num + 42

    return (a, x)

if test:
    test_case_count = 4000
    success = 0
    failures = []

    for i in range(0, test_case_count):
        size = i % 3000
        test_case = generate_test_case(size)
        (a, x) = test_case
        actual = binary_search(a, x)
        correct = True
        if actual == -1:
            if x in a:
                correct = False
        elif actual < 0 or actual >= len(a) or a[actual] != x:
            correct = False

        if not (correct):
            failures.append((test_case, actual))
        else: 
            success += 1

    failed = len(failures)
    print("Success: {0}, Failed: {1}".format(success, failed))
    print("")
    if failed == 0:
        print("Success")
    else:
        print("FAILED!!!")
        print("Failed Test Cases:")         
        for ((a, x, index), actual) in failures:
            print("%s | %s | %s | %s" % (a, x, index, actual))
else:
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[n + 1]
    a = data[1 : n + 1]
    for x in data[n + 2:]:
        # replace with the call to binary_search when implemented
        print(binary_search(a, x), end = ' ')
