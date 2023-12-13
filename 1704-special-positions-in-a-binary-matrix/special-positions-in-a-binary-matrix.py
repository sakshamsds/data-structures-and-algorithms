class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        # brute force
        m, n = len(mat), len(mat[0])
        res = 0
        for r in range(m):
            for c in range(n):
                if mat[r][c] == 1:
                    extra_1 = False
                    for c0 in range(n):
                        if c0 != c and mat[r][c0] == 1:
                            extra_1 = True
                            break
                    for r0 in range(m):
                        if r0 != r and mat[r0][c] == 1:
                            extra_1 = True
                            break
                    if not extra_1:
                        res += 1

        return res
