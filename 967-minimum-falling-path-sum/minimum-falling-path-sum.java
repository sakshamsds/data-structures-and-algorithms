class Solution {
    public int minFallingPathSum(int[][] matrix) {
        int n = matrix.length;
        for (int r = 1; r < n; r++) {
            matrix[r][0] += Math.min(matrix[r - 1][0], matrix[r - 1][1]);
            matrix[r][n - 1] += Math.min(matrix[r - 1][n - 1], matrix[r - 1][n - 2]);
            for (int c = 1; c < n - 1; c++) {
                matrix[r][c] += Math.min(matrix[r - 1][c - 1], Math.min(
                                        matrix[r - 1][c],
                                        matrix[r - 1][c + 1]));
            }
        }
        int minSum = matrix[n - 1][0];
        for (int c = 1; c < n; c++) {
            minSum = Math.min(minSum, matrix[n - 1][c]);
        }
        return minSum;
    }
}