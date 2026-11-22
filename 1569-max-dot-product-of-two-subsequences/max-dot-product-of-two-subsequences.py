class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        if max(nums1) < 0 and min(nums2) > 0:
            return max(nums1) * min(nums2)
        if max(nums2) < 0 and min(nums1) > 0:
            return max(nums2) * min(nums1)

        cache = {}
        def dfs(i, j):
            if i == len(nums1) or j == len(nums2):
                return 0

            if (i, j) in cache:
                return cache[(i, j)]
            
            maxPdt = max(
                        dfs(i + 1, j),
                        dfs(i, j + 1),
                        dfs(i + 1, j + 1) + nums1[i] * nums2[j]
                    )
                
            cache[(i, j)] = maxPdt
            return maxPdt

        return dfs(0, 0)