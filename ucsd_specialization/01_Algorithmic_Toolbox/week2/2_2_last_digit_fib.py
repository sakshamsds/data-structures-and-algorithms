
def last_digit_fib_num(n):
    # create an array of n
    fib = []
    fib.append(0)
    fib.append(1)
    for i in range(2, n+1):
        fib.append((fib[i-1] + fib[i-2]) % 10)
    return fib[n] % 10

if __name__ == '__main__':
    input_n = int(input())
    # input_n = 613455
    # input_n = 91239
    print(last_digit_fib_num(input_n))
