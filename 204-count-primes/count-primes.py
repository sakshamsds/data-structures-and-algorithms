class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 3:
            return 0

        primes = [1] * n
        div = 2
        while div * div < n:
            if primes[div]:
                for num in range(div * div, n, div):
                    primes[num] = 0
            div += 1

        return sum(primes[2:])