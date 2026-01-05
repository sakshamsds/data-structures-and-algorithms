class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        # pass negative sign to the smallest value
        n = len(matrix)
        num_neg, smallest_value = 0, 10 ** 5
        matrix_sum = 0

        for r in range(n):
            for c in range(n):
                num = matrix[r][c]
                smallest_value = min(smallest_value, abs(num))
                if num < 0:
                    num_neg += 1
                matrix_sum += abs(num)

        # print(matrix_sum, smallest_value)
        return matrix_sum if num_neg % 2 == 0 else matrix_sum - 2 * smallest_value