package leetcode.datastructures.medium;

import java.util.HashSet;
import java.util.Set;

// https://leetcode.com/problems/valid-sudoku/
// 36. Valid Sudoku

public class ValidSuduko {
	public static void main(String[] args) {

		/*
		 * Constraints
		 * 
		 * board.length == 9, board[i].length == 9, board[i][j] is a digit 1-9 or '.'.
		 */

		char[][] board = new char[][] { { '5', '3', '.', '.', '7', '.', '.', '.', '.' },
										{ '6', '.', '.', '1', '9', '5', '.', '.', '.' }, 
										{ '.', '9', '8', '.', '.', '.', '.', '6', '.' },
										{ '8', '.', '.', '.', '6', '.', '.', '.', '3' }, 
										{ '4', '.', '.', '8', '.', '3', '.', '.', '1' },
										{ '7', '.', '.', '.', '2', '.', '.', '.', '6' },
										{ '.', '6', '.', '.', '.', '.', '2', '8', '.' },
										{ '.', '.', '.', '4', '1', '9', '.', '.', '5' }, 
										{ '.', '.', '.', '.', '8', '.', '.', '7', '9' } };

		System.out.println(isValidSudoku(board));
	}
	
	public static boolean isValidSudoku(char[][] board) {

		// brute force
		// check along rows, no repetition of words
		// check along columns
		// check for mini cubes and check validity

		for (int i = 0; i < 9; i++) {
			Set<Character> rowSet = new HashSet<>();
			Set<Character> colSet = new HashSet<>();
			Set<Character> cubeSet = new HashSet<>();
			
			for (int j = 0; j < 9; j++) {

				// 1. check duplicates along rows
				if (board[i][j] != '.' && rowSet.add(board[i][j]) == false) {
					return false;
				}

				// 2. check duplicates along columns
				if (board[j][i] != '.' && colSet.add(board[j][i]) == false) {
					return false;
				}
				
				// 3. check duplicates in cube
				// trick is to iterate the cube
				/*
				0|1|2
				3|4|5
				6|7|8
				*/
				// we divide the suduku in 3/3 matrix using i
				int cubeRow = (i/3)*3 + j/3;
				int cubeCol = (i%3)*3 + j%3;
				if (board[cubeRow][cubeCol] != '.' && cubeSet.add(board[cubeRow][cubeCol]) == false) {
					return false;
				}
				
			}
		}
		
		return true;
		
		// test
//		int iteration = 0;
//		for (int i = 0; i < 9; i++) {
//			for (int j = 0; j < 9; j++) {
//				
//				/*
//				0|1|2
//				3|4|5
//				6|7|8
//				 */
//				
//				// we divide the suduku in 3/3 matrix using i
//				
//				int row = (i/3)*3 + j/3;
//				int col = (i%3)*3 + j%3;
//				System.out.print(row + "," + col + "\t");
//				
//				iteration++;
//				if (iteration == 9) {
//					iteration = 0;
//					System.out.println();
//				}
//			}
//		}
		
	}

}
