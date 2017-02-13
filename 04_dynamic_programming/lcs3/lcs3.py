#Uses python3

import sys

def lcs3(first, second, third):
    m = len(first)
    n = len(second)
    p = len(third)

    # init
    d = [0] * (p + 1)
    for k in range(0, p + 1):
        d[k] = [0] * (n + 1)
        for j in range(0, n + 1):
            d[k][j] = [0] * (m + 1)

    # fill
    for k in range(1, p + 1):
        for j in range(1, m + 1):
            for i in range(1, n + 1):
                if second[i - 1] == first[j - 1] == third[k - 1]:
                    d[k][i][j] = d[k - 1][i - 1][j - 1] + 1
                else:
                    d[k][i][j] = max(d[k][i][j - 1], d[k][i - 1][j], d[k - 1][i][j])

    # backtrack
    # find k first
    dmax, pmax = -1, -1
    for k in range(1, p+1):
        if d[k][n][m] > dmax:
            dmax = d[k][n][m]
            pmax = k

    # init rest
    common = [None] * dmax
    c_index = dmax - 1
    k, i, j = pmax, n, m
    # finally, the backtrack
    while k > 0 and i > 0 and j > 0:
        if first[j - 1] == second[i - 1] == third[k - 1]:
            common[c_index], c_index = first[j - 1], c_index - 1
            k, i, j = k - 1, i - 1, j - 1
        else:
            options = [
                (d[k - 1][i][j], (k - 1, i, j)),
                (d[k][i - 1][j], (k, i - 1, j)),
                (d[k][i][j - 1], (k, i, j - 1)),
            ]
            options.sort(key=lambda x: x[0], reverse=True)
            k, i, j = options[0][1]

    return common

#main
input = sys.stdin.read()
data = list(map(int, input.split()))
an = data[0]
data = data[1:]
a = data[:an]
data = data[an:]
bn = data[0]
data = data[1:]
b = data[:bn]
data = data[bn:]
cn = data[0]
data = data[1:]
c = data[:cn]
print(len(lcs3(a, b, c)))
