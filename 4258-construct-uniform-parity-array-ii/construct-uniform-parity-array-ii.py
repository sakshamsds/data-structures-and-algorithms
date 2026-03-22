class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        if min(nums1) & 1 == 1:
            return True

        num_odd, num_even = 0, 0
        for num in nums1:
            num_odd += 1 if num & 1 == 1 else 0
            num_even += 1 if num & 1 == 0 else 0

        return num_odd == len(nums1) or num_even == len(nums1)