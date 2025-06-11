class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        # try to make the rightmost element in the window

        nums.sort()
        l, res, window_sum = 0, 0, 0

        for r in range(len(nums)):
            window_sum += nums[r]

            while (r - l + 1) * nums[r] > window_sum + k:
                window_sum -= nums[l]
                l += 1

            res = max(res, r - l + 1)
        
        return res
