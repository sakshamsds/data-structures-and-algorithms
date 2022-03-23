package easy;

// https://leetcode.com/problems/first-unique-character-in-a-string/
// 387. First Unique Character in a String

public class FirstUniqueCharacterInAString {

	public static void main(String[] args) {
		String s = "loveleetcode";
		System.out.println(firstUniqChar(s));
	}

	public static int firstUniqChar(String s) {
		// Solution 3
		int freq[] = new int[26];

		for (char i : s.toCharArray()) {
			freq[i - 'a']++;
		}

		for (int i = 0; i < s.length(); i++) {
			if (freq[s.charAt(i) - 'a'] == 1)
				return i;
		}
		return -1;
	}

//	public static int firstUniqChar(String s) {
//		// Solution 2
//		for (int i = 0; i < s.length(); i++) {
//			char c = s.charAt(i);
//			if (s.indexOf(c) == s.lastIndexOf(c)) {
//				return i;
//			}
//		}
//		
//		return -1;
//	}

//	public static int firstUniqChar(String s) {
//		
//		// use linked hashmap instead of normal one to main key order
//		Map<Character, Integer> freqMap = new LinkedHashMap<>();
//		
//		char uniqueChar;
//		
//		for (int i = 0; i < s.length(); i++) {
//			char c = s.charAt(i);
//			if (freqMap.containsKey(c)) {
//				freqMap.put(c, freqMap.get(c) + 1);
//			} else {
//				freqMap.put(c, 1);
//				uniqueChar = c;
//			}
//		}
//		
//		for (Map.Entry<Character, Integer> entry : freqMap.entrySet()) {
//			if (entry.getValue() == 1) {
//				return s.indexOf(entry.getKey());
//			}
//		}
//		
//		return -1;
//	}

}
