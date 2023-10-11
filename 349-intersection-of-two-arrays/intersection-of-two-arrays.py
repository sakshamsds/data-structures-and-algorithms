class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        store = set(nums1)
        res = []
        for num in nums2:
            if num in store:
                res.append(num)
                store.remove(num)

        return res