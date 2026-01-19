class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # put heights in the stack in non-decreasing order
        stack, largest = [], 0
        for i, height in enumerate(heights + [0]):
            prev_i = i      # prev_i is imp, extend cur to all the way back
            while stack and stack[-1][0] > height:
                prev_h, prev_i = stack.pop()
                largest = max(largest, prev_h * (i - prev_i))
            stack.append((height, prev_i)) 
        return largest