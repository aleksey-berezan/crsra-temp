# Uses python3
import sys

def get_change(m):
    rem = m
    count = 0

    for coin in [10, 5, 1]:
        count += rem // coin
        rem = rem % coin
        if rem == 0:
            break

    if rem != 0:
        raise Exception("Unable to calculate change. Input: {0}, count so far: {1}, still remaining: {2}".format(m, count, rem))
    return count

# main
input = input()
m = int(input)
print(get_change(m))