package easy;

import java.util.HashMap;
import java.util.Map;

// https://leetcode.com/problems/ransom-note/
// 383. Ransom Note

public class RansomNote383 {

    public static void main(String[] args) {

        String ransomNote = "aa";
        String magazine = "ab";

        System.out.println(canConstruct(ransomNote, magazine));
        System.out.println(canConstruct2(ransomNote, magazine));
    }

    public static boolean canConstruct(String ransomNote, String magazine) {
        Map<Character, Integer> freqMap = new HashMap<>();

        for (char c : magazine.toCharArray()) {
            freqMap.put(c, freqMap.getOrDefault(c, 0) + 1);
        }

        // System.out.println(freqMap);

        for (char c : ransomNote.toCharArray()) {
            int freq = freqMap.getOrDefault(c, 0);
            if (freq == 0) {
                return false;
            }
            freqMap.put(c, --freq);
        }

        // System.out.println(freqMap);
        return true;
    }

    // java 8 solution
    public static boolean canConstruct2(String ransomNote, String magazine) {
        int[] counts = new int[26];
        magazine.chars().forEach(c -> counts[c - 'a']++);
        // System.out.println(Arrays.toString(counts));
        return ransomNote.chars().allMatch(c -> counts[c-'a']-- > 0);
    }
}
