class Solution {
    public int minPartitions(String n) {
        int[] haves = new int[10];
        for (char c : n.toCharArray()) {
            haves[c - '0']++;
        }
        // System.out.println(Arrays.toString(haves));
        for (int i = 9; i >= 0; i--){
            if (haves[i] > 0) return i;
        }
        return 0;
    }
}