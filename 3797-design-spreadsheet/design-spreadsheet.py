class Spreadsheet:

    def __init__(self, rows: int):
        self.queries = dict()

    def _get_row_col(self, cell: str):
        row = int(cell[1:]) - 1
        col = ord(cell[0]) - int(ord('A'))
        return row, col

    def setCell(self, cell: str, value: int) -> None:
        row, col = self._get_row_col(cell)
        self.queries[(row, col)] = value

    def resetCell(self, cell: str) -> None:
        row, col = self._get_row_col(cell)
        if (row, col) in self.queries:
            self.queries.pop((row, col))

    def getValue(self, formula: str) -> int:
        x, y = formula[1:].split('+')
        val = 0
        if x.isnumeric():
            val += int(x)
        else:
            rx, cx = self._get_row_col(x)
            val += self.queries.get((rx, cx), 0)

        if y.isnumeric():
            val += int(y)
        else:
            ry, cy = self._get_row_col(y)
            val += self.queries.get((ry, cy), 0)

        return val
        


# Your Spreadsheet object will be instantiated and called as such:
# obj = Spreadsheet(rows)
# obj.setCell(cell,value)
# obj.resetCell(cell)
# param_3 = obj.getValue(formula)