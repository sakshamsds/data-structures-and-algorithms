'''
2, 2 -> total = 2^n = 4 - 2 = 2
n = 3, total = 2^3 = 8 - 3 = 5
'''

class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        n = len(nums)
        # convert every number to integer
        available = set()
        for binary in nums:
            available.add(int(binary, 2))
        # print(available)

        max_num = 2 ** n
        for num in range(max_num):    # for n = 2, available should be 0, 1, 2, 3
            if num not in available:
                break

        # print(num)
        res = []
        while n > 0:
            res.append(str(num % 2))
            num //= 2
            n -= 1
        
        # print(res)
        return ''.join(res[::-1])
