#Uses python3
import sys


# memoized: map<input->sequence>
def optimal_sequence_internal(n, memo):
    if n in memo:
        return memo[n]
    if n == 1:
        prev,count = (0,0)
        memo[1] = (prev,count)
        return memo[1]

    sub_results = [None] * 3
    sub_results[0] = (n - 1, optimal_sequence_internal(n - 1, memo))
    sub_results[1] = (n // 2, optimal_sequence_internal(n // 2, memo)) if n % 2 == 0 else None
    sub_results[2] = (n // 3, optimal_sequence_internal(n // 3, memo)) if n % 3 == 0 else None

    sub_results = list([x for x in sub_results if x != None])
    sub_results.sort(key = lambda x:x[1][1], reverse=False)

    prev, count = sub_results[0]
    memo[n] = (prev, memo[prev][1]+1)

    return memo[n]

def optimal_sequence_internal2(n, memo):
    prev, count = optimal_sequence_internal(n, memo)

    sequence = [0] * (count+1)
    sequence[0] = n
    pr = prev
    i = 1
    while pr > 0:
        sequence[i] = pr
        pr, cnt = memo[pr]


        i += 1
    return reversed(sequence)

def optimal_sequence(n):
    memo = {}
    for i in range(1, n+1):
        optimal_sequence_internal(i, memo)
    prev, count = memo[n]

    sequence = [0] * (count+1)
    sequence[0] = n
    pr = prev
    i = 1
    while pr > 0:
        sequence[i] = pr
        pr, cnt = memo[pr]


        i += 1
    return reversed(sequence)

def optimal_sequence_naive(n):
    sequence = []
    while n >= 1:
        sequence.append(n)
        if n % 3 == 0:
            n = n // 3
        elif n % 2 == 0:
            n = n // 2
        else:
            n = n - 1
    return reversed(sequence)

# main

input = input()
n = int(input)
sequence = list(optimal_sequence(n))
print(len(sequence) - 1)
for x in sequence:
    print(x, end=' ')
