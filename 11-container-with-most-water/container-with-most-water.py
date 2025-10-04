class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        mx_water = 0

        while l < r:
            # print(mx_water, l, r)
            mx_water = max(mx_water, (r - l) * min(height[r], height[l]))
            if height[l] <= height[r]:
                l += 1
            else:
                r -= 1

        return mx_water