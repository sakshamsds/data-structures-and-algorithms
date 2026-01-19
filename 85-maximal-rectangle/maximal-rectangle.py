class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        # find largest histogram at every row
        rows, cols = len(matrix), len(matrix[0])

        def largest_histogram(heights):
            stack, largest = [], 0
            for i, height in enumerate(heights + [0]):
                start = i
                while stack and stack[-1][0] > height:
                    prev_h, start = stack.pop()
                    largest = max(largest, prev_h * (i - start))
                stack.append((height, start))
            return largest

        maximal_rect = 0
        prev = [0] * cols
        for r in range(rows):
            nxt = [0] * cols
            for c in range(cols):
                nxt[c] = prev[c] + 1 if matrix[r][c] == '1' else 0
            maximal_rect = max(maximal_rect, largest_histogram(nxt))
            # print(nxt, largest_histogram(nxt))
            prev = nxt

        return maximal_rect