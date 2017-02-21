# Uses python3
import sys

def optimal_weight(W, weights):
    n = len(weights)
    memo = [0] * (W + 1)
    for i in range(0, W + 1):
        memo[i] = [0] * (n + 1)

    for i in range(1, n + 1):
        for w in range(1, W + 1):
            memo[w][i] = memo[w][i - 1]
            wi = weights[i - 1]
            if wi <= w:
                val = memo[w - wi][i - 1] + wi
                if memo[w][i] < val:
                    memo[w][i] = val

    return memo[W][n]

# test
test = False
if test:
    test_cases = [
        (10, [1, 4, 8], 9),
        (10, [1, 8], 9),
        (10, [3, 5, 3, 3, 5], 10),
    ]

    for (W, weights, expected) in test_cases:
        actual = optimal_weight(W, weights)
        if actual != expected:
            print("Failed for {0}. Expected: {1}, Actual: {2}".format((W, weights), expected, actual))
        else: print("success")
else:
    # main
    lines = sys.stdin.readlines()
    input = '\n'.join(lines)

    W, n, *weights = list(map(int, input.split()))
    print(optimal_weight(W, weights))
