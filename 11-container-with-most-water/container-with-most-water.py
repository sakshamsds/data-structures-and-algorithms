class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        max_water = 0

        while l < r:
            cur_water = min(height[l], height[r]) * (r - l)   
            max_water = max(max_water, cur_water)
            if height[l] >= height[r]:
                r -= 1
            else:
                l += 1

        return max_water