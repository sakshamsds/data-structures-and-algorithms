class Solution:
    def isHappy(self, n: int) -> bool:
        visit = set()

        while n not in visit:
            visit.add(n)
            # print(visit)
            n = self.sum_of_squares(n)
            if n == 1:
                return True
        
        return False

    @staticmethod
    def sum_of_squares(n):
        sum = 0
        while n > 0:
            digit = n % 10
            sum += digit ** 2
            n //= 10
        return sum

