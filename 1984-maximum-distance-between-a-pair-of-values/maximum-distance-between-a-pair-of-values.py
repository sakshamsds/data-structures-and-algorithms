class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        r = len(nums2) - 1
        max_distance = 0
        for l in range(len(nums1) - 1, -1, -1):
            while l <= r and nums1[l] > nums2[r]:
                r -= 1
            max_distance = max(max_distance, r - l)
        return max_distance
        