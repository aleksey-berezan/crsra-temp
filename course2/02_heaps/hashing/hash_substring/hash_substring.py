# python3

p = 1000000007
x = 263


def read_input():
    return (input().rstrip(), input().rstrip())


def print_occurrences(output):
    print(' '.join(map(str, output)))


def hash_code(s):
    ans = 0
    for c in reversed(s):
        ans = (ans * x + ord(c)) % p
    return ans

def precompute_hashes(pattern, text):
    t_len = len(text)
    p_len = len(pattern)

    s = text[t_len - p_len:t_len]
    h = [None] * (t_len - p_len + 1)
    h[t_len - p_len] = hash_code(s)
    y = 1
    for i in range(1, p_len + 1):
        y = (y * x) % p

    for i in range(t_len - p_len - 1, -1, -1):
        h[i] = (x * h[i + 1] + ord(text[i]) - y * ord(text[i + p_len])) % p
    return h

def get_occurrences(pattern, text):
    t_len = len(text)
    p_len = len(pattern)
    if t_len < p_len:
        return []

    p_hash = hash_code(pattern)
    h = precompute_hashes(pattern, text)

    result = []
    for i in range(0, t_len - p_len+1):
        if p_hash != h[i]:
            continue
        if text[i:i + p_len] == pattern:
            result.append(i)

    return result

pattern, text = read_input()

occurences = get_occurrences(pattern, text)
print_occurrences(occurences)
