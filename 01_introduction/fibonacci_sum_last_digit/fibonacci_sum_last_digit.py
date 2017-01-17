# Uses python3
import sys

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

def fibonacci_sum(n):
    if n <= 1:
        return n
    m = 10
    pisanoSequence = get_pisano_sequence(m)
    pn = len(pisanoSequence)

    sum = 0
    for x in pisanoSequence:
        sum = (sum + x % m) % m

    for i in range(0,n % pn + 1):
        sum = (sum + pisanoSequence[i] % m) % m
    return sum

n = int(input())
print(fibonacci_sum(n))