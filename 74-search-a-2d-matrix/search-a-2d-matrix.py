class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])

        # find row in the matrix
        l, r = 0, rows - 1
        while l < r:
            mid = l + (r - l) // 2
            if matrix[mid][-1] < target:
                l = mid + 1
            else:
                r = mid
        row = l

        # find column in that row
        l, r = 0, cols - 1
        while l < r:
            mid = l + (r - l) // 2
            if matrix[row][mid] < target:
                l = mid + 1
            else:
                r = mid

        return matrix[row][l] == target