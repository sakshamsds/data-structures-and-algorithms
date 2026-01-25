class Solution {
    public boolean mergeTriplets(int[][] triplets, int[] target) {
        int px = 0, py = 0, pz = 0;
        for (int[] t : triplets) {
            if (t[0] <= target[0] && t[1] <= target[1] && t[2] <= target[2]) {
                px = Math.max(px, t[0]);
                py = Math.max(py, t[1]);
                pz = Math.max(pz, t[2]);
            }
        }
        return px == target[0] && py == target[1] && pz == target[2];
    }
}