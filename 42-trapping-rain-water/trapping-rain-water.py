class Solution:
    def trap(self, height: List[int]) -> int:
        lMax, rMax = height[0], height[-1]
        l, r = 0, len(height) - 1

        waterTrapped = 0
        while l <= r:
            if lMax < rMax:
                lMax = max(lMax, height[l])
                waterTrapped += lMax - height[l]
                l += 1                
            else:
                rMax = max(rMax, height[r])
                waterTrapped += rMax - height[r]
                r -= 1

        return waterTrapped



