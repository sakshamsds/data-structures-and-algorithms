class Spreadsheet:

    def __init__(self, rows: int):
        self.matrix = [[0] * 26 for _ in range(rows)]

    def _get_row_col(self, cell: str):
        row = int(cell[1:]) - 1
        col = int(ord('A') - ord(cell[0]))
        return row, col

    def setCell(self, cell: str, value: int) -> None:
        row, col = self._get_row_col(cell)
        self.matrix[row][col] = value

    def resetCell(self, cell: str) -> None:
        self.setCell(cell, 0)

    def getValue(self, formula: str) -> int:
        x, y = formula[1:].split('+')
        val = 0
        if 'A' <= x[0] <= 'Z':
            rx, cx = self._get_row_col(x)
            val += self.matrix[rx][cx]
        else:
            val += int(x)

        if 'A' <= y[0] <= 'Z':
            ry, cy = self._get_row_col(y)
            val += self.matrix[ry][cy]
        else:
            val += int(y)

        return val
        


# Your Spreadsheet object will be instantiated and called as such:
# obj = Spreadsheet(rows)
# obj.setCell(cell,value)
# obj.resetCell(cell)
# param_3 = obj.getValue(formula)