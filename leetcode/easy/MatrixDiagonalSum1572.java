package easy;

// 1572. Matrix Diagonal Sum
// https://leetcode.com/problems/matrix-diagonal-sum/

public class MatrixDiagonalSum1572 {
    public static void main(String[] args) {
        int[][] mat = new int[][] { { 1, 2, 3 }, { 4, 5, 6 }, { 7, 8, 9 } };
        System.out.println(new MatrixDiagonalSum1572().diagonalSum(mat));
    }

    public int diagonalSum(int[][] mat) {
        int sum = 0;
        int size = mat.length;
        for (int i = 0; i < size; i++) {
            sum += mat[i][i] + mat[size - i - 1][i];
        }

        if (size % 2 != 0) {
            sum -= mat[size / 2][size / 2];
        }

        return sum;
    }
}
