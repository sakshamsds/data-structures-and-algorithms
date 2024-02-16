class Solution:
    def addDigits(self, num: int) -> int:
        if num // 10 == 0:
            return num
        cur_sum = 0
        while num > 0:
            cur_sum += num % 10
            num //= 10
        return self.addDigits(cur_sum)