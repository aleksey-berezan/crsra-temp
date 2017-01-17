# Uses python3
import sys

def get_fibonacci_last_digit_naive(n):
    if n <= 1:
        return n

    previous = 0
    current  = 1

    for _ in range(n - 1):
        previous, current = current % 10, (previous + current) % 10

    return current

def get_fibonacci_last_digit(n):
    if n <= 1:
        return n

    previous = 0
    current  = 1

    for _ in range(n - 1):
        previous, current = current % 10, (previous + current) % 10

    return current

# main
# n = int(input())
# print(get_fibonacci_last_digit_naive(n))

# testing
for i in range(0,20):
    left = get_fibonacci_last_digit_naive(i)
    right = get_fibonacci_last_digit(i)
    if left != right:
        print("[FAIL] " + str(i) + ": " + str(left) + " != " + str(right))
    else: print("[ OK ] " + str(i) + ": " + str(left) + " == " + str(right))
