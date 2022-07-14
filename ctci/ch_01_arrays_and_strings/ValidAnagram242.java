package ch_01_arrays_and_strings;

public class ValidAnagram242 {
    public static void main(String[] args) {
        System.out.println(isAnagram("gamma", "alpha"));
        System.out.println(isAnagram("anagram", "nagaram"));
    }

    static boolean isAnagram(String s, String t) {
        // store character count in array from first string, 128
        // remove character count from array for second string
        // -ve count mean not an anagram

        if (s.length() != t.length()) {
            return false;
        }

        // assumption is that only ascii characters allowed
        // for leetcode problem only lowercase english are allowed
        int[] freq = new int[26];

        for (int i = 0; i < s.length(); i++) {
            int val1 = s.charAt(i);
            int val2 = t.charAt(i);
            freq[val1 - 'a']++;
            freq[val2 - 'a']--;
        }

        for (int i = 0; i < 26; i++) {
            if (freq[i] != 0) {
                return false;
            }
        }

        return true;
    }
}
