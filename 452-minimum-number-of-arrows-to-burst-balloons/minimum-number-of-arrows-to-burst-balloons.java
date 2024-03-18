class Solution {
    public int findMinArrowShots(int[][] points) {
        Arrays.sort(points, (a, b) -> Integer.compare(a[1], b[1]));
        // Arrays.sort(points, (a, b) -> a[1] - b[1]);
        int pos = points[0][1], shots = 1;
        for (int i = 0; i < points.length; i++) {
            if (pos < points[i][0]) {
                shots++;
                pos = points[i][1];
            }
        }
        return shots;
    }
}