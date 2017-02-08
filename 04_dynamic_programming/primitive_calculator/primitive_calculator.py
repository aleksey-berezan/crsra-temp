#Uses python3
import sys

def min_by_snd(left, right):
    _, lcount = left
    _, rcount = right
    return left if lcount < rcount else right

# memoized: map<input->sequence>
def optimal_sequence_internal(n, memo):
    if memo[n] != -1:
        prev, count = memo[n]
        return count

    prev, count = n - 1, optimal_sequence_internal(n - 1, memo)
    if n % 2 == 0:
        prev2, count2 = n // 2, optimal_sequence_internal(n // 2, memo)
        prev, count = min_by_snd((prev, count),(prev2, count2))

    if n % 3 == 0:
        prev3, count3 = n // 3, optimal_sequence_internal(n // 3, memo)
        prev, count = min_by_snd((prev, count),(prev3, count3))

    memo[n] = (prev, count + 1)
    return count + 1

def optimal_sequence(n):
    memo = [-1] * (n+1)
    memo[0] = memo[1] = (0,0)
    for i in range(1, n + 1):
        optimal_sequence_internal(i, memo)

    prev, count = memo[n]
    sequence = [0] * (count + 1)
    sequence[0] = n
    i = 1
    while prev > 0:
        sequence[i] = prev
        prev, _ = memo[prev]
        i += 1
    return reversed(sequence)

# main

input = input()
n = int(input)
sequence = list(optimal_sequence(n))
print(len(sequence) - 1)
for x in sequence:
    print(x, end=' ')
