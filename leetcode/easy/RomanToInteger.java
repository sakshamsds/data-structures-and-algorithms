package easy;

// https://leetcode.com/problems/roman-to-integer/
// 13. Roman to Integer

public class RomanToInteger {

	public static void main(String[] args) {

		String s = "LVIII";

		// convert to int array
		int[] ar = stringToIntArray(s);

		// if succeeding letter is bigger then use subtraction in the expression and
		// move to next letter
		// if succeeding letter is smaller then add to sum and move to next letter
		// determine value of every expression
		// add all values

		int sum = 0;
		int index = 0;
		
		while(index < ar.length) {
//			System.out.println(index);
			
			if (index + 1 == ar.length) {
				// means we are at last index
				// check value and add to sum
				// just add the value 
				sum += ar[index];
			} else {
				int currentValue = ar[index];
				int nextValue = ar[index + 1];

				if (nextValue <= currentValue) {
					sum += currentValue;
				} else {
					// evaluate expression and increment index by 2
					sum += nextValue - currentValue;
					index++;
				}
			}
			index++;
		}
		
		System.out.println(sum);

	}

	public static int[] stringToIntArray(String s) {
		int[] ar = new int[s.length()];

		for (int i = 0; i < s.length(); i++) {
			switch (s.charAt(i)){
				case 'I':
					ar[i] = 1;
					break;
				case 'V':
					ar[i] = 5;
					break;
				case 'X':
					ar[i] = 10;
					break;
				case 'L':
					ar[i] = 50;
					break;
				case 'C':
					ar[i] = 100;
					break;
				case 'D':
					ar[i] = 500;
					break;
				case 'M':
					ar[i] = 1000;
					break;
			}
		}
		return ar;
	}
}
