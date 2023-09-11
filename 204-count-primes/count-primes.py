class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 2:
            return 0

        primes = [0, 0]  + [1] * (n - 2)
        
        i = 2
        while i*i < n:
            for j in range(2*i, n, i):
                primes[j] = 0       # not a prime
            i += 1
                
        # print(primes)
        return sum(primes)
        