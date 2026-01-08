class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        cache = {}
        def dfs(i, j):
            if i == len(nums1) or j == len(nums2):
                return 0

            if (i, j) in cache:
                return cache[(i, j)]

            max_pdt = float(-inf)
            max_pdt = max(
                dfs(i + 1, j),
                dfs(i, j + 1),
                nums1[i] * nums2[j] + dfs(i + 1, j + 1)
            )
            cache[(i, j)] = max_pdt
            return max_pdt

        if max(nums1) < 0 and min(nums2) > 0:
            return max(nums1) * min(nums2)

        if max(nums2) < 0 and min(nums1) > 0:
            return max(nums2) * min(nums1)
        
        return dfs(0, 0)