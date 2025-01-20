class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        rows, cols = len(mat), len(mat[0])

        rows_count = [cols] * rows
        cols_count = [rows] * cols

        reverse_mapping = dict()
        for r in range(rows):
            for c in range(cols):
                reverse_mapping[mat[r][c]] = (r, c)

        for i, num in enumerate(arr):
            r, c = reverse_mapping[num]
            rows_count[r] -= 1
            cols_count[c] -= 1
            if rows_count[r] == 0 or cols_count[c] == 0:
                return i
        
        return -1