class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        # convert every number to string an find the length

        cnt = 0
        for num in nums:
            if len(str(num)) % 2 == 0:
                cnt += 1

        return cnt