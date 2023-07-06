
def get_pisano_period(m=10):
    prev, curr = 0, 1
    for i in range(0, m * m):
        prev, curr = curr, (prev + curr) % m

        # pisano number starts with 01
        if prev == 0 and curr == 1:
            return i+1
    return 60
    
def fib_sum(n):
    pp = get_pisano_period(10)
    n = n % pp

    if n <= 1:
        return n

    prev, cur, sum = 0, 1, 1
    for _ in range(2, n+1):
        prev, cur = cur, (prev + cur) % 10
        sum += cur
    return sum % 10

if __name__ == '__main__':
    input_n = int(input())
    # input_n = 100
    # input_n = 240
    # input_n = 832564823476
    print(fib_sum(input_n))
