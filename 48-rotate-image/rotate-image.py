class Solution:
    def rotate(self, m: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        n = len(m)
        for i in range(n//2):
            for j in range(i, n - i - 1):
                temp = m[n - j - 1][i]      # save bottom left
                m[n - j - 1][i] = m[n - i - 1][n - j - 1]       # update bottom left
                m[n - i - 1][n - j - 1] = m[j][n - i - 1]       # update bottom right
                m[j][n - i - 1] = m[i][j]   # update top right
                m[i][j] = temp      # update top left
                
        