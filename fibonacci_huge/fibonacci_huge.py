# Uses python3
import sys

def calc_fib(n):
    if (n <= 1):
        return n
    if (n == 2):
        return 1
    xi1 = 1
    xi = 2
    for i in range(3,n):
        xi1, xi = xi, xi1 + xi
    return xi

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
            return index - 1

    raise Exception("Unable to find repeating sequence for sequence with len " + str(len(nums)))

def get_pisano_pediod(m):
    size = max(m*5, 1000)
    mods = size * [0]
    mods[0] = 0
    mods[1] = 1

    for i in range(2, size):
        mods[i] = (mods[i-1] + mods[i-2]) % m

    return find_repeating_sequence(mods)

def get_fibonacci_huge(n, m):
    pn = get_pisano_pediod(m)
    r = n % pn
    fib = calc_fib(r)
    return fib % m

# main
input = input()
n, m = map(int, input.split())
print (get_fibonacci_huge(n, m))