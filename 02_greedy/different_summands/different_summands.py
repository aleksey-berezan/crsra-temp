# Uses python3
import sys

def optimal_summands(n):
    summands = []

    k = n
    l = 1
    while True:
        if k <= 2 * l:
            summands.append(k)
            break
        summands.append(l)
        (k, l) = (k - l, l + 1)

    #write your code here
    return summands

# main
input = input()
n = int(input)
summands = optimal_summands(n)
print(len(summands))
for x in summands:
    print(x, end=' ')
