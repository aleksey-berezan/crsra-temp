# Uses python3

def edit_distance(left, right):
    n = len(right)
    m = len(left)
    distance = [0] * (n + 1)
    for j in range(0, n + 1):
        distance[j] = [0] * (m + 1)
        distance[j][0] = j
    for i in range(0, m + 1):
        distance[0][i] = i

    for j in range(1, m + 1):
        for i in range(1, n + 1):
            if right[i - 1] == left[j - 1]:
                distance[i][j] = distance[i - 1][j - 1]
            else:
                insertion = distance[i][j - 1]
                deletion = distance[i - 1][j]
                mismatch = distance[i - 1][j - 1]
                distance[i][j] = 1 + min(insertion, deletion, mismatch)

    return distance[n][m]

# main
print(edit_distance(input(), input()))
