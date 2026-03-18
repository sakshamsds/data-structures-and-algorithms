class Solution {
    public int countSubmatrices(int[][] grid, int k) {
        int rows = grid.length, cols = grid[0].length;
        int res = (grid[0][0]) <= k ? 1 : 0;

        // iterate first row
        for (int c = 1; c < cols; c++) {
            grid[0][c] += grid[0][c - 1];
            if (grid[0][c] > k) break;
            res += 1;
        }

        // iterate first column
        for (int r = 1; r < rows; r++) {
            grid[r][0] += grid[r - 1][0];
            if (grid[r][0] > k) break;
            res += 1;
        }

        // iterate rest
        for (int r = 1; r < rows; r++) {
            if (grid[r][0] > k) break;
            for (int c = 1; c < cols; c++) {
                grid[r][c] += grid[r - 1][c] + grid[r][c - 1] - grid[r - 1][c - 1];
                if (grid[r][c] > k) break;
                res += 1; 
            }
        }

        return res;
    }
}