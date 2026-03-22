class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        if min(nums1) & 1 == 1:
            return True

        for num in nums1:
            if num & 1 == 1:
                return False
        return True