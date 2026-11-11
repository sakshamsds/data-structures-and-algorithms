class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        stack = []      # h, i
        maxArea = 0
        for i, h in enumerate(heights + [0]):
            prevI = i
            while stack and stack[-1][0] > h:
                prevH, prevI = stack.pop()
                maxArea = max(
                    maxArea, 
                    (i - prevI + 1) * h,
                    (i - prevI) * prevH
                )
            stack.append((h, min(prevI, i)))
        return maxArea
            
