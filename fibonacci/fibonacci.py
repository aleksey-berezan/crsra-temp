# Uses python3
def calc_fib(n):
    if (n <= 1):
        return n

    return calc_fib(n - 1) + calc_fib(n - 2)

def calc_fib2(n):
    if (n <= 1):
        return n
    if (n == 2):
        return 1
    xi1 = 1
    xi = 2
    for i in range(3,n):
        xi1, xi = xi % 10, (xi1 + xi) % 10
    
    return xi

# testing
for i in range(0,20):
    left = calc_fib(i)
    right = calc_fib2(i)
    if left != right:
        print("[FAIL] " + str(i) + ": " + str(left) + " != " + str(right))
    else: print("[ OK ] " + str(i) + ": " + str(left) + " == " + str(right))

#n = int(input())
#print(calc_fib(n))
