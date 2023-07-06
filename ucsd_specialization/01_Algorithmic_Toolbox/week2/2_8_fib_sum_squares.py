
# f1**2 + f2**2 + .... + fn**2 = fn*fn+1

def get_pisano_period(m):
    prev, curr = 0, 1
    for i in range(0, m * m):
        prev, curr = curr, (prev + curr) % m

        # pisano number starts with 01
        if prev == 0 and curr == 1:
            return i+1
    return 60
        
def huge_fib(n, m=10):
    # piasano period
    pp = get_pisano_period(m)
    n = n % pp
    if n<=1:
        return n
    previous = 0
    current = 1
    for _ in range(2, n+1):
        previous, current = current, (previous + current) % m
    return current


if __name__ == '__main__':
    n = int(input())
    # n = 1234567890
    print(huge_fib(n)*huge_fib(n+1)%10)
