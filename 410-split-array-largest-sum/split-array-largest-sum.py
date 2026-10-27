class Solution:
    def splitArray(self, nums: list[int], k: int) -> int:
        l, r = max(nums), sum(nums)

        def isValid(largest):
            splits = 1
            curSum = 0
            for num in nums:
                curSum += num
                if curSum > largest:
                    curSum = num
                    splits += 1
            return splits <= k

        while l < r:
            mid = l + (r - l) // 2
            if isValid(mid):
                r = mid
            else:
                l = mid + 1

        return l