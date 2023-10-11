class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums1) > len(nums2):
            return self.intersect(nums2, nums1)

        freq_map = collections.Counter(nums1)
        # print(freq_map)
        
        res = []
        for num in nums2:
            if freq_map[num] > 0:
                res.append(num)
                freq_map[num] -= 1
        
        
        return res