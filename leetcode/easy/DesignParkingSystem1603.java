package easy;

public class DesignParkingSystem1603 {
    public static void main(String[] args) {

    }

}

class ParkingSystem {

    private int[] count;

    public ParkingSystem(int big, int medium, int small) {
        count = new int[3];
        count[0] = big;
        count[1] = medium;
        count[2] = small;
    }

    // big = 1, medium = 2, small = 3
    public boolean addCar(int carType) {
        if (count[carType - 1] > 0) {
            count[carType - 1]--;
            return true;
        }
        return false;
    }
}
