class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[0] * n for _ in range(n)]
        directions = deque(['R', 'D', 'L', 'U'])
        r_low, r_high, c_low, c_high = 0, n - 1, 0, n - 1
        cur_num, n_squared = 1, n * n
        while cur_num <= n_squared:
            cur_dir = directions.popleft()
            if cur_dir == 'R':     
                for c in range(c_low, c_high + 1):
                    matrix[r_low][c] = cur_num
                    cur_num += 1
                r_low += 1
            elif cur_dir == 'D':   
                for r in range(r_low, r_high + 1): 
                    matrix[r][c_high] = cur_num
                    cur_num += 1
                c_high -= 1
            elif cur_dir == 'L': 
                for c in range(c_high, c_low - 1, -1):
                    matrix[r_high][c] = cur_num
                    cur_num += 1
                r_high -= 1
            else:           
                for r in range(r_high, r_low - 1, -1): 
                    matrix[r][c_low] = cur_num
                    cur_num += 1
                c_low += 1
            directions.append(cur_dir)

        return matrix