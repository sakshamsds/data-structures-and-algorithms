class Solution:
    def trap(self, height: List[int]) -> int:
        max_left, max_right = 0, 0
        left, right = 0, len(height) - 1

        water_trapped = 0

        while left <= right:
            max_left = max(max_left, height[left])
            max_right = max(max_right, height[right])

            if max_left < max_right:
                water_trapped += max_left - height[left]
                left += 1
            else:
                water_trapped += max_right - height[right]
                right -= 1
            
        return water_trapped
