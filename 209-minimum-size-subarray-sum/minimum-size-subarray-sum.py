class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        curSum = 0
        minSize = len(nums) + 1
        for r, num in enumerate(nums):
            curSum += num
            while curSum >= target:
                minSize = min(minSize, r - l + 1)
                curSum -= nums[l]
                l += 1

        return 0 if minSize == len(nums) + 1 else minSize 