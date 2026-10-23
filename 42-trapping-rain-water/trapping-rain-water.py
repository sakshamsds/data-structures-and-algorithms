class Solution:
    def trap(self, heights: list[int]) -> int:
        left, right = 0, len(heights) - 1  # pointers
        leftMax, rightMax = 0, 0  # max heights
        water = 0

        while left < right:  # compare pointers
            leftMax = max(leftMax, heights[left])
            rightMax = max(rightMax, heights[right])

            if heights[left] < heights[right]:
                water += max(0, min(leftMax, rightMax) - heights[left])
                left += 1
            else:
                water += max(0, min(leftMax, rightMax) - heights[right])
                right -= 1

        return water
