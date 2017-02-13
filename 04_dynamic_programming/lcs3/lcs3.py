#Uses python3

import sys

def get_edit_distance_matrix(first, second, third):
    m = len(first)
    n = len(second)
    p = len(third)

    d = [0] * (p + 1)#[0] * (n + 1)
    for k in range(0, p + 1):
        d[k] = [0] * (n + 1)
        for j in range(0, n + 1):
            d[k][j] = [0] * (m + 1)
        #d[j][0] = j
    #for i in range(0, m + 1):
        #d[0][i] = i
    for k in range(1, p + 1):
        for j in range(1, m + 1):
            for i in range(1, n + 1):
                if second[i - 1] == first[j - 1] == third[k - 1]:
                    d[k][i][j] = d[k - 1][i - 1][j - 1] + 1
                else:
                    insertion1 = d[k][i][j - 1]
                    deletion1 = d[k][i - 1][j]
                    insertion2 = d[k-1][i][j - 1]
                    deletion2 = d[k-1][i - 1][j]
                    # mismatch = d[i - 1][j - 1]
                    d[k][i][j] = max(insertion1, deletion1, insertion2, deletion2)#, mismatch)

    #return d[n][m]

    # backtrack
    common = [None] * d[p][n][m]
    c_index = d[p][n][m] - 1
    k, i, j = p, n, m
    while k > 0 and i > 0 and j > 0:
        if first[j - 1] == second[i - 1] == third[k - 1]:#d[i][j] > d[i-1][j-1]:
            common[c_index], c_index = first[j - 1], c_index - 1
            k, i, j = k - 1, i - 1, j - 1
        else:
            options = [
                (d[k-1][i][j], (k-1,i,j)),
                (d[k][i-1][j], (k,i-1,j)),
                (d[k][i][j-1], (k,i,j-1)),
            ]
            options.sort(key=lambda x: x[0], reverse=True)
            k,i,j = options[0][1]
            # if d[i-1][j] > d[i][j]-1:
            #     i -= 1
            # else:
            #     j -= 1

    return common
    #return d

def lcs3(a, b, c):
    common = get_edit_distance_matrix(a,b,c)
    return common
    # return "".join([str(x) for x in common])

test = True
if test:
    test_cases = [#("abcdaf", "acbcf", ""),
                  ((['a', 'b', 'c', 'd', 'a', 'f'], ['a', 'c', 'b', 'c', 'f'], ['a', 'b', 'c', 'd', 'a', 'f']), ['a','b','c','f']),
                  ((['a', 'b', 'c', 'd', 'a', 'f'], ['a', 'c', 'b', 'c', 'f'], ['a', 'c', 'b', 'c', 'f']), ['a','b','c','f']),
                  ((list("123"), list("213"), list("135")), list("13")),
                  (([8, 3, 2, 1, 7], [8, 2, 1, 3, 8, 10, 7], [6, 8, 3, 1, 4, 7]), [8, 3, 7])]
    for (a,b,c),expected in test_cases:
        actual = lcs3(a,b,c)
        if actual != expected:
            print("FAIL. Expected: {0}, Actual: {1} for {2}".format(expected, actual, (a,b,c)))
        else:
            print("SUCCESS")
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
