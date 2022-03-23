package easy;

import java.util.Arrays;

// https://leetcode.com/problems/reshape-the-matrix/
// 566. Reshape the Matrix

public class ReshapeTheMatrix {

	public static void main(String[] args) {

		int[][] matrix = new int[][] { new int[] { 1, 2 }, new int[] { 3, 4 } };
		int r = 2;
		int c = 2;

		int[][] result = matrixReshape(matrix, r, c);
		System.out.println(Arrays.deepToString(result));
		System.out.println();
		System.out.println(Arrays.deepToString(result)
                .replace("],","\n").replace(",","\t| ")
                .replaceAll("[\\[\\]]", " "));
	}

	public static int[][] matrixReshape(int[][] mat, int r, int c) {
		// Solution 1, O(r*c);

		int numRows = mat.length;
		int numColumns = mat[0].length;

		if (numRows * numColumns != r * c) {
			return mat;
		} else {

			int[][] newMatrix = new int[r][c];

			int m = 0;
			int n = 0;

			for (int i = 0; i < r; i++) {
				for (int j = 0; j < c; j++) {
					if(n>=numColumns) {
						n = 0;
						m++;
					} 
					newMatrix[i][j] = mat[m][n];
					n++;
				}
			}
			return newMatrix;
		}
	}

}
