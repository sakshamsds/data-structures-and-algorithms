/*
        11  3
        11  3
       110
 */

class Solution {
    public String addBinary(String a, String b) {
        StringBuilder sb = new StringBuilder();
        int carry = 0;
        int i = 0;

        while (i < a.length() || i < b.length()) {
            int ai = a.length() - 1 - i;
            int bi = b.length() - 1 - i;

            int val1 = (ai >= 0) ? Character.getNumericValue(a.charAt(ai)) : 0;
            int val2 = (bi >= 0) ? Character.getNumericValue(b.charAt(bi)) : 0;
            int digit = val1 + val2 + carry;
            carry = (digit > 1) ? 1 : 0;
            digit %= 2;
            sb.append(String.valueOf(digit));
            i++;
        }

        if (carry == 1) sb.append(String.valueOf(carry));
        sb.reverse();
        return sb.toString();
    }

}