
def get_pisano_period(m):
    prev, curr = 0, 1
    for i in range(0, m * m):
        prev, curr = curr, (prev + curr) % m

        # pisano number starts with 01
        if prev == 0 and curr == 1:
            return i+1
        
# print(get_pisano_period(2))
# print(get_pisano_period(3))
# print(get_pisano_period(5))
# print(get_pisano_period(10))

def huge_fib(n, m):
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

if __name__ == "__main__":
    n, m = map(int, input().split())
    # n, m = 2816213588, 239
    # n, m = 115, 1000
    # n, m = 1, 239
    # n, m = 10, 2
    # n ,m = 9999999999999, 2
    print(huge_fib(n, m))

