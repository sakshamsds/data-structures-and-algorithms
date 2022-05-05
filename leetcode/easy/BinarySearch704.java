package easy;

public class BinarySearch704 {
    public static void main(String[] args) {
        System.out.println(new BinarySearch704().search(new int[] { -1, 0, 3, 5, 9, 12 }, 9));
        System.out.println(new BinarySearch704().search(new int[] { -1, 0, 3, 5, 9, 12 }, 2));
    }

    // iterative
    public int search(int[] nums, int target) {
        int start = 0;
        int end = nums.length - 1;
        while (start <= end) {
            int midIdx = (start + end) / 2;
            if (nums[midIdx] == target) {
                return midIdx;
            } else if (nums[midIdx] < target) {
                start = midIdx + 1;
            } else {
                end = midIdx - 1;
            }
        }
        return -1;
    }

    // // recursive
    // public int search(int[] nums, int target) {
    // return helper(nums, 0, nums.length - 1, target);
    // }

    // public int helper(int[] nums, int start, int end, int target) {
    // System.out.println("start: " + start + " end: " + end);
    // int midIdx = (start + end) / 2;
    // if (target == nums[midIdx]) {
    // return midIdx;
    // }

    // if (start < end) {
    // if (target > nums[midIdx]) {
    // return helper(nums, midIdx + 1, end, target);
    // } else {
    // return helper(nums, start, midIdx - 1, target);
    // }
    // } else {
    // return -1;
    // }
    // }
}
