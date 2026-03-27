class Solution {
    public boolean areSimilar(int[][] mat, int k) {
        int rows = mat.length;
        int cols = mat[0].length;

        if (k % cols == 0) {
            return true;
        }
        k = k % cols;

        for (int r = 0; r < rows; r++) {
            int right = k;
            if (r % 2 == 1) right = cols - k;

            for (int left = 0; left < cols; left++) {
                if (mat[r][left] != mat[r][right]) return false;
                right += 1;
                if (right == cols) right = 0;
            }
        }

        return true;
    }
}