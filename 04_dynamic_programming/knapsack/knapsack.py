# Uses python3
import sys

def optimal_weight_greedy(W, weights):
    # write your code here
    result = 0
    for x in weights:
        if result + x <= W:
            result = result + x
    return result

def but_last(items):
    if len(items) > 0:
        return items[:len(items)-1]

    raise Exception("Empty list is not allowed")

def optimal_weight_internal(W, weights, memo):


    n = len(weights)
    current = optimal_weight_internal(W, but_last(weights), memo)
    return memo(W, n)

def get_value(memo, w, i):
    #return memo[w-1][i-1]
    return memo[i][w]
def set_value(memo, w, i, value):
    #memo[w-1][i-1] = value
    memo[i][w] = value

def optimal_weight(W, weights):
    n = len(weights)
    memo = [0] * (n+1)
    for i in range(0,n+1):
        memo[i] = [0] * (W+1)
    # memo = [([0] * W+1)] * len(weights)

    # for j in range(0, n):
    #     memo[0][j] = 0
    # for w in range(0, W):
    #     memo[0][w] = 0

    #
    # for w in range(1, W + 1):
    #     for i in range(1, n + 1):
    #         memo[i][w] = 0

    for i in range(1, n + 1):
        for w in range(1, W + 1):
            set_value(memo, w, i, get_value(memo, w, i - 1))# memo[w][i] = memo[w][i - 1]
            wi = weights[i - 1]# prev
            if wi <= w:
                val = get_value(memo, w - wi, i - 1) + wi   # memo[w - wi][i - 1] + wi
                if get_value(memo, w, i) < val:             # if memo[w][i] < val:
                    set_value(memo, w, i, val)              #     memo[w][i] = val

    return get_value(memo, W, n)#memo[W][n]

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
