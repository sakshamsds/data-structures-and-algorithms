class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        # start with zeros and make string different from every num
        n = len(nums)
        unique = ['0'] * n

        for i, num in enumerate(nums):
            if num[i] == unique[i]:
                unique[i] = '1'

        return ''.join(unique) 