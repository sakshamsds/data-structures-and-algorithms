class Solution {
    public boolean areSimilar(int[][] mat, int k) {
        int rows = mat.length;
        int cols = mat[0].length;

        if (k % cols == 0) {
            return true;
        }

        k = k % cols;

        // even matching
        for (int r = 0; r < rows; r += 2) {
            int right = k;
            for (int left = 0; left < cols; left++) {
                if (mat[r][left] != mat[r][right]) return false;
                right += 1;
                if (right == cols) right = 0;
            }
        }

        // odd matching
        for (int r = 1; r < rows; r += 2) {
            int right = cols - k;
            for (int left = 0; left < cols; left++) {
                if (mat[r][left] != mat[r][right]) return false;
                right += 1;
                if (right == cols) right = 0;
            }
        }
        
        return true;
    }
}