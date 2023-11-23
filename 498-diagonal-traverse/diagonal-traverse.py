class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        m, n = len(mat), len(mat[0])
        diag_dict = collections.defaultdict(list)
        for i in range(m):
            for j in range(n):
                diag_dict[i + j].append(mat[i][j])

        # print(diag_dict)
        res = []
        for k, v in diag_dict.items():
            if k % 2 == 1:
                res.extend(v)
            else:
                res.extend(v[::-1])

        return res
