class Solution {
    public int uniquePathsIII(int[][] grid) {
        int zeros = 0, sx = 0, sy = 0;
        for(int r = 0; r < grid.length; r++){
            for(int c = 0; c < grid[0].length; c++){
                if(grid[r][c] == 0){
                    zeros++;
                } else if(grid[r][c] == 1){
                    sx = r;
                    sy = c;
                }
            }
        }
        return dfs(grid, sx, sy, zeros);
    }

    private int dfs(int[][] grid, int x, int y, int zeros){
        if(x < 0 || y < 0 || x >= grid.length || y >= grid[0].length || grid[x][y] == -1){
            return 0;
        }
        if(grid[x][y] == 2){
            return zeros == -1 ? 1 : 0; 
        }
        grid[x][y] = -1;
        zeros--;
        int totalPaths = dfs(grid, x + 1, y, zeros) + 
                        dfs(grid, x, y + 1, zeros) + 
                        dfs(grid, x - 1, y, zeros) +
                        dfs(grid, x, y - 1, zeros);

        //backtrack
        grid[x][y] = 0;
        zeros++;
        return totalPaths;    
    }
}