class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        rows, cols = len(matrix), len(matrix[0])
        heights = [0] * cols
        self.maxArea = 0

        def getMax():
            stack = []      # (h, i)
            for i, h in enumerate(heights + [0]):
                prevI = i
                while stack and stack[-1][0] > h:
                    prevH, prevI = stack.pop()
                    self.maxArea = max(
                        self.maxArea,
                        (i - prevI) * prevH
                    )
                stack.append((h, prevI))

        for row in matrix:
            for i, num in enumerate(row):
                if num == '0':
                    heights[i] = 0
                else:
                    heights[i] += 1
            getMax()

        return self.maxArea
