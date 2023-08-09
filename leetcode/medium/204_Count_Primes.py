class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 2:
            return 0

        is_prime = [True] * n 
        for number in range(2, n):
            if is_prime[number]:     
                # eliminate till n 
                for multiple in range(number * number, n, number):      # https://leetcode.com/problems/count-primes/solutions/1353496/count-primes-for-kids/
                    is_prime[multiple] = False

        # print(is_prime)
        return sum(is_prime) - 2