class Solution:
    def minOperations(self, nums: list[int], x: int) -> int:
        # 11 - 5 = 6
        # largest subarray with sum = 6

        targetSum = sum(nums) - x
        n = len(nums)
        l = 0
        subarraySum = 0
        maxSize = -1
        for r in range(n):
            subarraySum += nums[r]
            while l <= r and subarraySum > targetSum:
                subarraySum -= nums[l]
                l += 1
            if subarraySum == targetSum:
                maxSize = max(maxSize, r - l + 1)

        # print(maxSize)
        return n - maxSize if maxSize > -1 else -1

            
