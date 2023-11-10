class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        res = 0
        for num in nums:
            div = set()
            for i in range(1, floor(sqrt(num)) + 1):    # trick is to reduce this computation by sqrt(n)
                if num % i == 0:
                    div.add(i)
                    div.add(num // i)
                if len(div) > 4:
                    break

            print(div)
            if len(div) == 4:
                res += sum(div)
        return res