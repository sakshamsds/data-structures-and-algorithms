package easy;

// https://leetcode.com/problems/reverse-words-in-a-string-iii/
// 557. Reverse Words in a String III

public class ReverseWordsInString557 {
    public static void main(String[] args) {
        System.out.println(new ReverseWordsInString557().reverseWords("Let's take LeetCode contest"));
    }

    public String reverseWords(String s) {
        StringBuffer buffer = new StringBuffer();
        String[] words = s.split(" ");

        for (String word : words) {
            for (int i = 0; i < word.length(); i++) {
                buffer.append(word.charAt(word.length() - i - 1));
            }
            buffer.append(" ");
        }
        buffer.setLength(buffer.length() - 1);
        return buffer.toString();
    }

}
