class Solution:
    def rotate(self, m: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        # Time Complexity = O(n ^ 2)
        # one pass
        n = len(m)
        for r in range(n//2 + n%2):
            for c in range(n//2):
                tmp = m[r][c]
                m[r][c] = m[n - c - 1][r]
                m[n - c - 1][r] = m[n - r - 1][n - c - 1]
                m[n - r - 1][n - c - 1] = m[c][n - r - 1]
                m[c][n - r - 1] = tmp

        # two pass
        # n = len(m)
        # # self.print_mat(m)

        # # swap along main diagonal
        # for r in range(n):
        #     for c in range(n - r):
        #         m[r][c], m[n-c-1][n-r-1] = m[n-c-1][n-r-1], m[r][c]
        # # self.print_mat(m)

        # # swap along horizontal axis
        # for r in range(n//2):
        #     for c in range(n):
        #         m[r][c], m[n-r-1][c] = m[n-r-1][c], m[r][c]

        # # self.print_mat(m)


        
    # def print_mat(self, matrix: List[List[int]]) -> None:
    #     print()
    #     for r in matrix:
    #         print(r)
        