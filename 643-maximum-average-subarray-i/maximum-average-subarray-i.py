class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        max_sum = cur_sum = sum(nums[:k])
        for right in range(k, len(nums)):
            cur_sum += nums[right] - nums[right - k]
            max_sum = max(cur_sum, max_sum)

        return max_sum/k