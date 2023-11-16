'''
2, 2 -> total = 2^n = 4 - 2 = 2
n = 3, total = 2^3 = 8 - 3 = 5
'''

class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        n = len(nums)
        available = set()
        for binary in nums:
            available.add(int(binary, 2))

        for num in range(n + 1):    # for n = 2, available should be 0, 1, 2, 3
            if num not in available:
                return bin(num)[2:].zfill(n)