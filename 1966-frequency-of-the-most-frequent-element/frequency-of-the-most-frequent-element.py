class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        # sliding window approach
        # number we trying to make is the last number in the window
        nums.sort()
        res, l, window_sum = 0, 0, 0

        for r in range(len(nums)):
            window_sum += nums[r]
            # condition: sum of window + k >= size of window * max_num
            # editorial: we will not shrink the window - we will just try to grow it as large as we can
            if window_sum + k < (r - l + 1) * nums[r]:
                window_sum -= nums[l]
                l += 1

        return r - l + 1