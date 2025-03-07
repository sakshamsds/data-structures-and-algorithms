class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        primes = [True] * (right + 1)
        primes[0] = primes[1] = False

        div = 2
        while div * div <= right:
            if primes[div]:
                for num in range(div * div, right + 1, div):
                    primes[num] = False
            div += 1

        prev = None
        min_diff = float('inf')
        res = [-1, -1]
        for num in range(left, right + 1):
            if primes[num]:
                if prev and num - prev < min_diff:
                    res = [prev, num]
                    min_diff = num - prev
                prev = num
        return res



        

        