class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        for i in range(9):
            rowSet = set()
            colSet = set()
            box = set()            
            for j in range(9):
                if board[i][j] != '.' and board[i][j] in rowSet:
                    return False
                rowSet.add(board[i][j])

                if board[j][i] != '.' and board[j][i] in colSet:
                    return False
                colSet.add(board[j][i])

                '''
                j 012 -> 0
                j 345 -> 1
                j 678 -> 2
                r = (r // 3) * 3 + j // 3 
                c = (r % 3) * 3 + j % 3
                '''
                r = (i // 3) * 3 + j // 3 
                c = (i % 3) * 3 + j % 3
                if board[r][c] != '.' and board[r][c] in box:
                    return False
                box.add(board[r][c])
        return True