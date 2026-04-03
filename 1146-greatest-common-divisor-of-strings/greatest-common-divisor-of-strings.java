class Solution {
    public String gcdOfStrings(String str1, String str2) {
        for (int i = Math.min(str1.length(), str2.length()); i > 0; i--) {
            if (valid(str1, str2, i)) return str1.substring(0, i);
        }
        return "";
    }

    public boolean valid(String str1, String str2, int i) {
        int l1 = str1.length(), l2 = str2.length();
        if ((l1 % i != 0) && (l2 % i != 0)) return false;
        String base = str1.substring(0, i);
        return str1.replace(base, "").isEmpty() && str2.replace(base, "").isEmpty();
    }
}