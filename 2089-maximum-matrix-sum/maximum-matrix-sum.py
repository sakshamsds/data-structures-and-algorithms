class Solution:
    def maxMatrixSum(self, matrix: list[list[int]]) -> int:
        numNeg = 0
        minAbsVal, total = float('inf'), 0

        for row in matrix:
            for val in row:
                if val < 0:
                    numNeg += 1
                minAbsVal = min(minAbsVal, abs(val))
                total += abs(val)

        if minAbsVal == 0 or numNeg & 1 == 0:
            return total

        return total - 2 * minAbsVal

        


        