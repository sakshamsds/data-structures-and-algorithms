class Solution {
    public String decodeCiphertext(String encodedText, int rows) {
        int length = encodedText.length();
        int cols = length / rows;
        StringBuilder sb = new StringBuilder();

        for (int i = 0; i < cols; i++) {
            for (int j = i; j < length; j += cols + 1) {
                sb.append(encodedText.charAt(j));
                // if (j == length - 1) return sb.toString();
            }
        }

        return sb.toString().stripTrailing();
    }
}