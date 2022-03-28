package easy;

public class CheckIfStraightLine1232 {

    public static void main(String[] args) {

        int[][] coordinates = { { 0, 0 }, { 0, 1 }, { 0, -1 } };
        // int[][] coordinates = { { 1, 2 }, { 2, 3 }, { 3, 4 }, { 4, 5 }, { 5, 6 }, {
        // 6, 7 } };
        System.out.println(checkStraightLine(coordinates));

    }

    public static boolean checkStraightLine(int[][] coordinates) {

        double baseSlope = calculateSlope(coordinates[0][0], coordinates[1][0], coordinates[0][1], coordinates[1][1]);
        for (int i = 2; i < coordinates.length; i++) {
            double slope = calculateSlope(coordinates[0][0], coordinates[i][0], coordinates[0][1], coordinates[i][1]);
            if (baseSlope != slope)
                return false;
        }

        return true;
    }

    public static double calculateSlope(int x1, int x2, int y1, int y2) {
        if (x1 - x2 == 0)
            return Double.MAX_VALUE;
        return (double) (y1 - y2) / (x1 - x2);
    }

}
