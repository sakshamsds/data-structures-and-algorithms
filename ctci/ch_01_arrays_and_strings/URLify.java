package ch_01_arrays_and_strings;

public class URLify {
    public static void main(String[] args) {
        System.out.println(method(new char[] { 'a', ' ', 'c', ' ', ' ', ' ' }, 3));
    }

    static char[] method(char[] str, int trueLength) {
        int spaces = 0;
        for (int i = 0; i < trueLength; i++) {
            if (str[i] == ' ') {
                spaces++;
            }
        }

        int lastIndex = trueLength + spaces * 2;

        for (int i = trueLength - 1; i >= 0; i--) {
            if (str[i] == ' ') {
                str[lastIndex - 1] = '0';
                str[lastIndex - 2] = '2';
                str[lastIndex - 3] = '%';
                lastIndex -= 3;
            } else {
                str[lastIndex - 1] = str[i];
                lastIndex--;
            }

        }

        return str;
    }
}
