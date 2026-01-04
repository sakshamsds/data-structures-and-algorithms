class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        res = 0
        for num in nums:
            num_divisors, divisor_sum = 2, 1 + num
            i = 2
            while i * i <= num and num_divisors < 5:
                if num % i == 0:
                    div1, div2 = i, num // i
                    if div1 == div2:
                        num_divisors += 1
                        divisor_sum += div1
                    else:
                        num_divisors += 2
                        divisor_sum += div1 + div2
                i += 1
            
            if num_divisors == 4:
                res += divisor_sum

        return res
