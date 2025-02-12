class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        zeros, start = 0, 0
        max_ones = 0

        for end in range(len(nums)):
            if nums[end] == 0:
                zeros += 1

            if zeros > k:
                if nums[start] == 0:
                    zeros -= 1
                start += 1

            max_ones = max(max_ones, end - start + 1)
        return max_ones

            