#Uses python3

import sys

def get_edit_distance_matrix(left, right):
    n = len(right)
    m = len(left)
    d = [0] * (n + 1)
    for j in range(0, n + 1):
        d[j] = [0] * (m + 1)
        #d[j][0] = j
    #for i in range(0, m + 1):
        #d[0][i] = i

    for j in range(1, m + 1):
        for i in range(1, n + 1):
            if right[i - 1] == left[j - 1]:
                d[i][j] = d[i - 1][j - 1] + 1
            else:
                insertion = d[i][j - 1]
                deletion = d[i - 1][j]
                # mismatch = d[i - 1][j - 1]
                d[i][j] = max(insertion, deletion)#, mismatch)

    #return d[n][m]
    # backtrack

    common = [None] * d[n][m]
    c_index = d[n][m] - 1
    i, j = n, m
    while i > 0 and j > 0:
        if left[j - 1] == right[i - 1]:#d[i][j] > d[i-1][j-1]:
            common[c_index], c_index = left[j - 1], c_index - 1
            i,j = i - 1, j - 1
        else:
            if d[i-1][j] > d[i][j]-1:
                i -= 1
            else:
                j -= 1

    return common
    #return d

def lcs3(a, b, c):
    common = get_edit_distance_matrix(a,b)

    #write your code here
    return min(len(a), len(b), len(c))

test = True
if test:
    test_cases = [("abcdaf", "acbcf", "")
        ]
    for (a,b,c) in test_cases:
        actual = lcs3(a,b,c)
else:
    #main
    #if __name__ == '__main__':
    input = input()#sys.stdin.read()
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
    print(lcs3(a, b, c))
