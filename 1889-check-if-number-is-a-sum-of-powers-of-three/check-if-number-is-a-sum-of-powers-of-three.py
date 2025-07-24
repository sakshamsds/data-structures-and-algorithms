class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        # editorial comment

        while n > 1:
            if n % 3 == 0 or (n - 1) % 3 == 0:
                n //= 3
            else:
                return False

        return True