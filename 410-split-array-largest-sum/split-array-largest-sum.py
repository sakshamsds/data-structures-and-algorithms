'''
    max splits = len(nums), largestSum = max(nums)
    min splits = 0, largestSum = sum(nums)

    binary search on largestSum
'''

class Solution:
    def splitArray(self, nums: list[int], k: int) -> int:
        l, r = max(nums), sum(nums)

        def isValid(lSum):
            curSum, splits = 0, 1
            for num in nums:
                curSum += num
                if curSum > lSum:
                    splits += 1
                    curSum = num
            return splits <= k

        while l < r:
            mid = l + (r - l) // 2

            if isValid(mid):
                r = mid
            else:
                l = mid + 1

        return l
