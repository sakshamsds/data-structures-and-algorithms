class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        s1, s2 = sum(nums1), sum(nums2)
        z1, z2 = nums1.count(0), nums2.count(0)

        if (z1 == 0 and z2 + s2 > s1) or (z2 == 0 and z1 + s1 > s2):
            return -1
        
        return max(s1 + z1, s2 + z2)