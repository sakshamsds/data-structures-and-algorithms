class Solution {
    public String addBinary(String a, String b) {
        StringBuilder sb = new StringBuilder();
        int carry = 0;
        int ai = a.length() - 1;
        int bi = b.length() - 1;

        while (ai >= 0 || bi >= 0 || carry > 0) {
            carry += (ai >= 0) ? Character.getNumericValue(a.charAt(ai)) : 0;
            carry += (bi >= 0) ? Character.getNumericValue(b.charAt(bi)) : 0;
            sb.append(String.valueOf(carry % 2));
            carry /= 2;
            ai--;
            bi--;
        }
        return sb.reverse().toString();
    }

}