package easy;

// https://leetcode.com/problems/decrypt-string-from-alphabet-to-integer-mapping/
// 1309. Decrypt String from Alphabet to Integer Mapping

public class Decryption1309 {
    public static void main(String[] args) {
        // System.out.println((int) '1');
        // System.out.println((int) '0');
        // System.out.println((int) 'a');
        // System.out.println((char) ('a' + Integer.valueOf(11) - 1));
        // System.out.println((int) ('1'));
        // System.out.println((char) ('a' + '2' - '1'));
        // System.out.println();

        System.out.println(new Decryption1309().freqAlphabets("10#11#12"));
    }

    public String freqAlphabets(String s) {
        StringBuffer output = new StringBuffer();
        // traverse in reverse
        for (int i = s.length() - 1; i > -1; i--) {
            char c = s.charAt(i);
            // System.out.println(c);
            if (c == '#') {
                String sub = s.substring(i - 2, i);
                // System.out.println(sub);
                output.insert(0, (char) ('a' + Integer.valueOf(sub) - 1));
                i -= 2;
            } else {
                output.insert(0, (char) ('a' + c - '1'));
            }
        }
        return output.toString();
    }
}
