'''
have a [-1, -1] and [-1, -1]T filter and apply multiple times
number negatives 
'''
class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        count_neg = 0
        abs_sum, abs_min = 0, 10 ** 5
        
        rows, cols = len(matrix), len(matrix[0])
        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] < 0:
                    count_neg += 1
                abs_min = min(abs_min, abs(matrix[r][c]))
                abs_sum += abs(matrix[r][c])

        if count_neg % 2 == 0:
            return abs_sum
        return abs_sum - 2 * abs_min