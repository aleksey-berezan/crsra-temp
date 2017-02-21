# Uses python3
import sys

def getRatio(item):
    (v,w,ratio) = item
    return ratio

def pack(weights, values):
    packed = []
    for i in range(0, len(weights)):
        x = (values[i], weights[i], values[i] / weights[i])
        packed.append(x)
    packed.sort(key=getRatio,reverse=True)
    return packed

def get_optimal_value(capacity, weights, values):
    value = 0.

    rem = capacity
    packed = pack(weights, values)
    for v, w, ratio in packed:
        if rem == 0:
            break
        take = min(rem, w)
        value += take * ratio
        rem -= take

    return round(value, 4)

# main
lines = sys.stdin.readlines()
input = '\n'.join(lines)
data = list(map(int, input.split()))
n, capacity = data[0:2]
values = data[2:(2 * n + 2):2]
weights = data[3:(2 * n + 2):2]
opt_value = get_optimal_value(capacity, weights, values)
print("{:.10f}".format(opt_value))