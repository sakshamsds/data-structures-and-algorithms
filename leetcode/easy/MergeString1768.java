package easy;

// 1768. Merge Strings Alternately
// https://leetcode.com/problems/merge-strings-alternately/

public class MergeString1768 {
    public static void main(String[] args) {
        String word1 = "abcd";
        String word2 = "pq";
        System.out.println(new MergeString1768().mergeAlternately("abc", "pqr"));
        System.out.println(new MergeString1768().mergeAlternately("ab", "pqrs"));
        System.out.println(new MergeString1768().mergeAlternately(word1, word2));
    }

    public String mergeAlternately(String word1, String word2) {
        StringBuffer output = new StringBuffer();
        int l1 = word1.length();
        int l2 = word2.length();
        int min = Math.min(l1, l2);

        for (int i = 0; i < min; i++) {
            output.append(word1.charAt(i)).append(word2.charAt(i));
            l1--;
            l2--;
        }

        if (l1 == 0) {
            // add rest of word2
            return output.toString().concat(word2.substring(word1.length()));
        } else {
            // add rest of word1
            return output.toString().concat(word1.substring(word2.length()));
        }
    }
}
