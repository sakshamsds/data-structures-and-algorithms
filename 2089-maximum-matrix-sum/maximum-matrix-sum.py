class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        # if num neg is even then sum
        # if num neg is odd then min element
        # break up case - if min element is 0

        n = len(matrix)
        total = 0
        num_neg = 0
        min_val = abs(matrix[0][0])
        for row in matrix:
            for num in row:
                total += abs(num)
                num_neg += 1 if num < 0 else 0
                min_val = min(min_val, abs(num))

        if min_val == 0 or num_neg & 1 == 0:
            return total
        
        return total - 2 * min_val