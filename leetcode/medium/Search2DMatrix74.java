package medium;

// https://leetcode.com/problems/search-a-2d-matrix/
// 74. Search a 2D Matrix

public class Search2DMatrix74 {

	public static void main(String[] args) {

		int[][] matrix = new int[][] { { 1, 3, 5, 7 }, { 10, 11, 16, 20 }, { 23, 30, 34, 60 } };
		int target = 17;
		System.out.println(searchMatrix(matrix, target));

	}

	public static boolean searchMatrix(int[][] matrix, int target) {

		// binary search, O(logM + logN), O(logMN)
		int rows = matrix.length;
		int columns = matrix[0].length;

		int low = 0;
		int high = rows * columns - 1;

		while (low <= high) {
			int mid = low + (high - low) / 2;
			int value = matrix[mid / columns][mid % columns];

			if (value == target) {
				return true;
			} else if (value < target) {
				low = mid + 1;
			} else {
				high = mid - 1;
			}
		}

		return false;
	}

//	public static boolean searchMatrix(int[][] matrix, int target) {
//		
//		// search column wise, O(M+N)
//		
//		for (int row = 0; row < matrix.length; row++) {
//			
//			// if target is bigger than the last element of this row, then search in next
//			// row
//			if (target > matrix[row][matrix[0].length - 1]) {
//				continue;
//			} else {
//				for (int col = 0; col < matrix[0].length; col++) {
//					if (matrix[row][col] == target) {
//						return true;
//					}
//				}
//				return false;
//			}
//		}
//		
//		return false;
//	}

}
