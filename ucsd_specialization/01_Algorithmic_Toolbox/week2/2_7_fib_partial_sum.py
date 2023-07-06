
def get_pisano_period(m=10):
    prev, curr = 0, 1
    for i in range(0, m * m):
        prev, curr = curr, (prev + curr) % m

        # pisano number starts with 01
        if prev == 0 and curr == 1:
            return i+1

def fib_partial_sum(m, n):
    pp = get_pisano_period(10)
    m = m % pp
    n = n % pp

    if n<m:
        n+=60

    if n == 0:
        return 0

    prev, curr, sum = 0, 1, 0
    for i in range(n+1):
        if i>=m:
            sum+=prev
        prev, curr = curr, prev + curr
    return sum % 10

if __name__ == '__main__':
    m, n = map(int, input().split())
    print(fib_partial_sum(m, n))
    # print(fib_partial_sum(10, 10))
    # print(fib_partial_sum(3, 7))
    # print(fib_partial_sum(0, 239))
    # print(fib_partial_sum(1234, 12345))
    # print(fib_partial_sum(5618252, 6583591534156))
