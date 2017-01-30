# Uses python3
import sys
import random
import itertools

def get_sort_key(x):
    return x[0]

def merge(left, right):
    r = { }
    # print (left)
    for x, count in left:
        if x in r:
            r[x] += count
        else:
            r[x] = count
    for x, count in right:
        if x in r:
            r[x] += count
        else:
            r[x] = count
    result = list(r.items())
    # print("returning " + str(result))
    return result

def get_majority_element_internal(a, left, right):
    if left > right:
        return []

    if left == right:
        return [(a[left], 1)]
    if left + 1 == right:
        # print(a)
        # print(left)
        # print(right)
        if a[left] == a[right]:
            return [(a[left], 2)]
        else:
            return [(a[left], 1), (a[right], 1)]#.sort(key=get_sort_key)

    mid = (left + right) // 2
    left_results = get_majority_element_internal(a, left, mid)
    right_results = get_majority_element_internal(a, mid + 1, right)
    return merge(left_results, right_results)

def get_majority_element(a, left, right):
    merged = get_majority_element_internal(a, left, right)
    merged.sort(key=lambda x:x[1],reverse=True)
    # print("we've got: " +str(merged))
    if len(merged) == 0:
        return -1
    top_item,top_count = merged[0]
    return 1 if top_count > len(a) // 2 else -1

    # if right - left == 1:
    #     return 
    # if left == right:
    #     return -1
    # if left + 1 == right:
    #     return a[left]
    #write your code here
    return -1

def generate_test_array(size, has_majority_item):
    if size == 0:
        return []
    # size = 5
    min_num = 12
    max_num = 99
    majority_num = 11
    a = [0] * size
    for i in range(0, size):
        a[i] = random.randint(min_num,max_num)
    
    if has_majority_item:
        for i in range(0, (size // 2) + 1):
            a[i] = majority_num
    
    perms = list(itertools.permutations(a))
    return list(perms)[random.randint(0, len(perms)-1)]

test = False
if test:
    test_case_count = 100
    success = 0
    failures = []

    for i in range(0, test_case_count):
        size = max(1, i % 9)
        has_majority_item = i % 2 == 0
        test_array = generate_test_array(size, has_majority_item)
        a = test_array
        actual = get_majority_element(a, 0, len(a)-1)
        expected = 1 if has_majority_item else -1
        if actual != expected:
            failures.append((test_array, expected, actual))
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
        for test_array,expected,actual in failures:
            print("%s | %s | %s" % (test_array,expected,actual))
else:
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    if get_majority_element(a, 0, n-1) != -1:
        print(1)
    else:
        print(0)
