class Solution {
    public int numSpecial(int[][] mat) {
        int m = mat.length;
        int n = mat[0].length;
        int[] rowOnes = new int[m];
        int[] colOnes = new int[n];

        for (int r = 0; r < m; r++) {
            for (int c = 0; c < n; c++) {
                if (mat[r][c] == 1) {
                    rowOnes[r]++;
                    colOnes[c]++;
                }
            }
        }

        int count = 0;
        for (int r = 0; r < m; r++) {
            for (int c = 0; c < n; c++) {
                if (mat[r][c] == 1 && rowOnes[r] == 1 && colOnes[c] == 1) {
                    count++;
                }
            }
        }
        return count;
    }
}