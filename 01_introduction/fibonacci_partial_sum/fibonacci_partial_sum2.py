# Uses python3
import sys

def fibonacci_partial_sum_naive(from_, to):
    if to <= 1:
        return to

    previous = 0
    current = 1

    for _ in range(from_ - 1):
        # print(_)
        previous, current = current, previous + current
    # print("c")
    sum = current

    for _ in range(to - from_):
        previous, current = current, previous + current
        # print(current)
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

    raise Exception("Unable to find repeating sequence for sequence with len " + str(len(nums)))

def get_pisano_sequence(m):
    size = max(m * 5, 1000)
    mods = size * [0]
    mods[0] = 0
    mods[1] = 1

    for i in range(2, size):
        mods[i] = (mods[i-1] + mods[i-2]) % m

    return find_repeating_sequence(mods)

def summ(nums,mod):
    sum = 0
    for x in nums:
        sum = (sum + x % mod) % mod
    return sum

def fibonacci_partial_sum(m, n):
    if n <= 1:
        return n
    pnSeq = get_pisano_sequence(10)
    pn = len(pnSeq)

    # left part
    r = m % pn
    leftPart = pnSeq[r:]
    sum = summ(leftPart, 10)

    # main part
    mainStart = m + (pn - r)
    mainLen = n - mainStart + 1
    times = mainLen // pn
    pnSeqSum = (summ(pnSeq, 10) * times) % 10
    sum = (sum + pnSeqSum) % 10

    # right part
    rightLen = mainLen % pn
    rightPart = pnSeq[:rightLen]
    rightSum = summ(rightPart, 10)
    sum = (sum + rightSum) % 10
    return sum

# main
input = input()
from_, to = map(int, input.split())
print(fibonacci_partial_sum(from_, to))