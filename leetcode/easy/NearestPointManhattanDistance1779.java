package easy;

// https://leetcode.com/problems/find-nearest-point-that-has-the-same-x-or-y-coordinate/
// 1779. Find Nearest Point That Has the Same X or Y Coordinate

public class NearestPointManhattanDistance1779 {

    public static void main(String[] args) {
        int[][] points = { { 2, 3 } };
        // int[][] points = { { 3, 4 } };
        // int[][] points = { { 1, 2 }, { 3, 1 }, { 2, 4 }, { 2, 3 }, { 4, 4 } };
        int x = 3;
        int y = 4;
        System.out.println(nearestValidPoint(x, y, points));

    }

    public static int nearestValidPoint(int x, int y, int[][] points) {

        int minDistance = Integer.MAX_VALUE;
        int minDistanceIndex = -1;

        for (int row = 0; row < points.length; row++) {

            if (points[row][0] == x || points[row][1] == y) {
                // valid point
                // Manhattan distance
                int distance = Math.abs(points[row][0] - x) + Math.abs(points[row][1] - y);
                if (distance < minDistance) {
                    minDistance = distance;
                    minDistanceIndex = row;
                }

            }

        }

        return minDistanceIndex;
    }
}
