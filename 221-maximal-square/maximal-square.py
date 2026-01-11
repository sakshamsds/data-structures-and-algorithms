class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        rows, cols = len(matrix), len(matrix[0])

        prefix = [[0] * cols for _ in range(rows)]
        prefix[0][0] = int(matrix[0][0])

        for r in range(1, rows):
            prefix[r][0] = prefix[r - 1][0] + int(matrix[r][0])
        for c in range(1, cols):
            prefix[0][c] = prefix[0][c - 1] + int(matrix[0][c])
        for r in range(1, rows):
            for c in range(1, cols):
                prefix[r][c] = int(matrix[r][c]) + prefix[r][c - 1] + \
                                prefix[r - 1][c] - prefix[r - 1][c - 1]

        # for row in prefix:
            # print(row)

        largest = 0
        # traverse all diagonals for all numbers
        for r in range(rows):
            for c in range(cols):
                # print(r, c)
                # print('----')
                # find max in that diagonal
                top_r, top_c = r - 1, c - 1
                while top_r >= -1 and top_c >= -1:
                    top_left = prefix[top_r][top_c] if top_r >= 0 and top_c >= 0 else 0
                    top_right = prefix[top_r][c] if top_r >= 0 else 0
                    bottom_left = prefix[r][top_c] if top_c >= 0 else 0
                    area_sum = prefix[r][c] + top_left - top_right - bottom_left
                    # print(area_sum, (r - top_r) ** 2)
                    if area_sum == (r - top_r) ** 2:    # square matrix exist
                        largest = max(largest, area_sum)
                    top_r, top_c = top_r - 1, top_c - 1
                # print()

        return largest

