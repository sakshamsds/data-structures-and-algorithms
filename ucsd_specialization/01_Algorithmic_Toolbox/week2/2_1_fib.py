
def fibonacci_number(n):
    # create an array of n
    fib = []
    fib.append(0)
    fib.append(1)
    for i in range(2, n+1):
        fib.append(fib[i-1] + fib[i-2])
    return fib[n]

# def fibonacci_number(n):
#     if n <= 1:
#         return n
#     return fibonacci_number(n - 1) + fibonacci_number(n - 2)


if __name__ == '__main__':
    input_n = int(input())
    print(fibonacci_number(input_n))
