package easy;

// 709. To Lower Case
// https://leetcode.com/problems/to-lower-case/

public class ToLowerCase709 {
    public static void main(String[] args) {
        System.out.println((int) 'a');
        System.out.println((int) 'A');
        System.out.println((int) 'Z');
        System.out.println('a' - 'A');

        System.out.println(new ToLowerCase709().toLowerCase("Hello"));
    }

    public String toLowerCase(String s) {
        StringBuffer output = new StringBuffer();

        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            if (c >= 65 && c <= 90) {
                // uppercase
                c = (char) (c + 32);
            }
            output.append(c);
        }

        return output.toString();
    }
}
