class Solution {
    public int minFallingPathSum(int[][] grid) {
        int n = grid.length;

        for (int r = 1; r < n; r++) {
            int min1 = Integer.MAX_VALUE;
            int min2 = Integer.MAX_VALUE;
            for (int c = 0; c < n; c++) {
                if (min1 > grid[r - 1][c]) {
                    min2 = min1;
                    min1 = grid[r - 1][c];
                } else if (min2 > grid[r - 1][c]) {
                    min2 = grid[r - 1][c];
                }
            }
            
            for (int c = 0; c < n; c++) {
                if (grid[r - 1][c] == min1) {
                    grid[r][c] += min2;
                } else {
                    grid[r][c] += min1;
                }
            }
        }
        return Arrays.stream(grid[n - 1]).min().getAsInt();
    }
}