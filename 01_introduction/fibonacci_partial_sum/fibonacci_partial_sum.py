# Uses python3
import sys


def fibonacci_partial_sum_naive(from_, to):
    if to <= 1:
        return to

    previous = 0
    current = 1

    for _ in range(from_ - 1):
        previous, current = current, previous + current

    sum = current

    for _ in range(to - from_):
        previous, current = current, previous + current
        sum += current

    return sum % 10


def find_repeating_sequence(nums):
    if len(nums) <= 3:
        raise Exception("Too short sequence")

    index = -1
    seqLen = len(nums) - 1
    for i in range(2, seqLen):
        index = i
        for j in range(0, i - 1):
            leftIndex = j
            rightIndex = i + j - 1
            if rightIndex > seqLen:
                break
            left = nums[leftIndex]
            right = nums[rightIndex]
            if left != right:
                index = -1
                break
        if index != -1:
            return nums[0:index - 1]

    raise Exception("Unable to find repeating sequence for sequence with len "
                    + str(len(nums)))


def get_pisano_sequence(m):
    size = max(m * 5, 1000)
    mods = size * [0]
    mods[0] = 0
    mods[1] = 1

    for i in range(2, size):
        mods[i] = (mods[i - 1] + mods[i - 2]) % m

    return find_repeating_sequence(mods)

def mod_sum(nums, m):
    sum = 0
    for i in nums:
        sum = (sum + i % m) % m
    return sum

def fibonacci_partial_sum(m, n):
    if n <= 1:
        return n
    pSeq = get_pisano_sequence(10)
    print(str(pSeq))
    pn = len(pSeq)
    print(pn)

    startLen = m % pn
    slicedLeft = pSeq[startLen:]
    sum = mod_sum(slicedLeft,10)

    target = n - m - len(slicedLeft)
    pSeqSum = mod_sum(pSeq, 10)
    pSeqSum = (pSeqSum * (target // pn)) % 10

    sum = (sum + pSeqSum) % 10

    r = target % pn
    slicedRight = pSeq[:r]
    sum = (sum + mod_sum(slicedRight, 10)) % 10
    return sum

# main
# input = input()
# from_, to = map(int, input.split())
# print(fibonacci_partial_sum(from_, to))

# testing
def f(m, n):
    return "[{0},{1}]".format(m,n)

failed = 0
# for n in range(0, 5):
#     for m in range(0, n + 1):
m = 3
n = 7
left = fibonacci_partial_sum_naive(m, n)
right = fibonacci_partial_sum(m, n)
if left != right:
    failed += 1
    print("[FAIL] " + str(f(m, n)) + ": " + str(left) + " != " + str(right))
else:
    print("[ OK ] " + str(f(m, n)) + ": " + str(left) + " == " + str(right))

if failed == 0:
    print("Test successfull.")
else:
    print("Failed: {0} times.".format(failed))
