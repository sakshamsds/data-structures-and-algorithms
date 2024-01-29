class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        ROWS, COLS = len(matrix), len(matrix[0])
        for r in range(ROWS):
            for c in range(COLS):
                top = self.matrix[r - 1][c] if r > 0 else 0
                left = self.matrix[r][c - 1] if c > 0 else 0
                top_left = self.matrix[r - 1][c - 1] if min(r, c) > 0 else 0
                self.matrix[r][c] = matrix[r][c] + top + left - top_left

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        top = self.matrix[row1 - 1][col2] if row1 > 0 else 0
        left = self.matrix[row2][col1 - 1] if col1 > 0 else 0
        top_left = self.matrix[row1 - 1][col1 - 1] if min(row1, col1) > 0 else 0
        return self.matrix[row2][col2] - top - left + top_left
        
# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)