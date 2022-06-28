package medium;

import java.util.HashMap;
import java.util.HashSet;
import java.util.Map;
import java.util.Set;

// https://leetcode.com/problems/minimum-deletions-to-make-character-frequencies-unique/discuss/2207605/Clean-Java-Code-With-Step-By-Step-Explanation
// https://leetcode.com/problems/minimum-deletions-to-make-character-frequencies-unique/
// 1647. Minimum Deletions to Make Character Frequencies Unique

public class MinDeletions1647 {
    public static void main(String[] args) {
        String input = "ceabaacb";
        // String input = "aaabbbcc";
        // String input = "aab";

        System.out.println(new MinDeletions1647().minDeletions(input));
    }

    public int minDeletions(String s) {
        Map<Character, Integer> freqMap = new HashMap<>();
        for (char c : s.toCharArray()) {
            freqMap.put(c, freqMap.getOrDefault(c, 0) + 1);
        }
        // System.out.println(freqMap);

        int deletions = 0;
        Set<Integer> uniqFreq = new HashSet<>();

        for (int freq : freqMap.values()) {
            while (uniqFreq.contains(freq)) {
                deletions++;
                freq--;
            }

            if (freq > 0) {
                uniqFreq.add(freq);
            }
        }

        // System.out.println(uniqFreq);
        return deletions;
    }
}