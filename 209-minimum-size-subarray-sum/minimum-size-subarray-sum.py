class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_size = len(nums) + 1
        left = 0
        subarray_sum = 0
        for right in range(len(nums)):
            subarray_sum += nums[right]

            while subarray_sum >= target:        # goal, how much we can shrink this
                min_size = min(min_size, right - left + 1)
                subarray_sum -= nums[left]
                left += 1

        return min_size if min_size != len(nums) + 1 else 0