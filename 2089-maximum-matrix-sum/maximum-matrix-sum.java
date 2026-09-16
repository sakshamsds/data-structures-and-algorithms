class Solution {
    public long maxMatrixSum(int[][] matrix) {
        // migrate the negative sign
        int n = matrix.length;
        int num_neg = 0;
        long total = 0L;
        int min_abs_value = Integer.MAX_VALUE;

        for (int[] row : matrix) {
            for (int num : row) {
                if (num < 0) num_neg++;
                min_abs_value = Math.min(min_abs_value, Math.abs(num));
                total += Math.abs(num);
            }
        }

        if (num_neg % 2 == 0 || min_abs_value == 0) return total;
        return total - 2 * min_abs_value;
    }
}