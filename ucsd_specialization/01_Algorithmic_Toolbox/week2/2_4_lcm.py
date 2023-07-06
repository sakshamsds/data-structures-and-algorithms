
def get_gcd(a, b):
    if b == 0:
        return a
    return get_gcd(b, a%b)

def get_lcm(a, b):
    gcd = get_gcd(a, b)
    return a * b // gcd

if __name__ == "__main__":
    a, b = map(int, input().split())
    # a, b = 761457, 614573
    print(get_lcm(a, b))