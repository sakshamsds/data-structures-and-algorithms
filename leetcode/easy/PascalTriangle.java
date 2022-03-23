package easy;

import java.util.ArrayList;
import java.util.List;

// https://leetcode.com/problems/pascals-triangle/submissions/
// 118. Pascal's Triangle

public class PascalTriangle {

	public static void main(String[] args) {

		generate(1);
		generate(2);
		generate(3);
		generate(4);
		generate(5);
		generate(15);

	}

	public static List<List<Integer>> generate(int numRows) {
		// Solution 2 O(n^2)

		List<List<Integer>> bigList = new ArrayList<>();
		List<Integer> row = new ArrayList<>();
		row.add(1);
		bigList.add(row);

		for (int i = 1; i < numRows; i++) {
			row = new ArrayList<>();

			row.add(1);
			List<Integer> previousList = bigList.get(i-1);
			for (int j = 0; j < previousList.size() - 1; j++) {
				row.add(previousList.get(j) + previousList.get(j + 1));
			}
			row.add(1);

			bigList.add(row);
		}

//		System.out.println(bigList.toString());
		return bigList;
	}

//	public static List<List<Integer>> generate(int numRows) {
//		
//		// Solution 1: fails for numRows = 15;
//		
//		List<List<Integer>> bigList = new ArrayList<>();
//		
//		for (int i = 0; i <= numRows-1; i++) {
//			List<Integer> row = new ArrayList<>();
//			
//			for (int j = 0; j <= i; j++) {
//				// iCj,
//				// n=5, 5C0=1, 5C1=5, 5C2=10, 5C3=10, 5C4=5, 5C5=0;
//				// fast approach, rather than calculating all factorials, use previous result to calculate next
//				// using maths
//				combinatorial(i, j);
//				row.add(combinatorial(i, j));
//			}
//			
//			bigList.add(row);
//		}
//		
//		System.out.println(bigList.toString());
//		return bigList;
//	}
//	
//	public static long combinatorial(int n, int r) {
//		// ncr = n! / n-r! * r!
//		return factorial(n) / (factorial(n - r) * factorial(r));
//	}
//
//	public static long factorial(int x) {
//		long fact = 1;
//		for (int i = 1; i <= x; i++) {
//			fact *= i;
//		}
//		return fact;
//	}
}
