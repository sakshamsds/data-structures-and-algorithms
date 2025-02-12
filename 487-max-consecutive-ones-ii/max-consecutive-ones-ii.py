class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        start, zeros_idx = 0, -1
        max_ones = 0

        for end in range(len(nums)):
            if nums[end] == 0:
                if start <= zeros_idx:   # one zero already exists in cur subarray
                    start = zeros_idx + 1
                zeros_idx = end
            max_ones = max(max_ones, end - start + 1)
        return max_ones