package ch_01_arrays_and_strings;

public class IsUnique {
    public static void main(String[] args) {
        System.out.println(isUniqueChars("alpha"));
        System.out.println(isUniqueChars("beta"));
        System.out.println(isUniqueChars("gamma"));
    }

    static boolean isUniqueChars(String str) {
        // ASCII String - 128 characters
        // ASCII extended - 256 characters
        // Unicode String - 2^21 characters

        if (str.length() > 128) {
            return false;
        }
        boolean[] charSet = new boolean[128];

        for (int i = 0; i < str.length(); i++) {
            int val = str.charAt(i);
            if (charSet[val]) {
                return false;
            }
            charSet[val] = true;
        }

        return true;
    }
}
