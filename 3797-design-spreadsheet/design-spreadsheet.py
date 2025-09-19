class Spreadsheet:

    def __init__(self, rows: int):
        self.queries = collections.defaultdict(int)

    def setCell(self, cell: str, value: int) -> None:
        self.queries[cell] = value

    def resetCell(self, cell: str) -> None:
        self.setCell(cell, 0)

    def getValue(self, formula: str) -> int:
        x, y = formula[1:].split('+')

        if x.isnumeric():
            x = int(x)
        else:
            x = self.queries.get(x, 0)

        if y.isnumeric():
            y = int(y)
        else:
            y = self.queries.get(y, 0)

        return x + y
        


# Your Spreadsheet object will be instantiated and called as such:
# obj = Spreadsheet(rows)
# obj.setCell(cell,value)
# obj.resetCell(cell)
# param_3 = obj.getValue(formula)