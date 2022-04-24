package easy;

// https://leetcode.com/problems/majority-element/
// 169. Majority Element
// https://www.youtube.com/watch?v=AoX3BPWNnoE

public class MajorityElement169 {
    public static void main(String[] args) {
        System.out.println(new MajorityElement169().majorityElement(new int[] { 3, 2, 3 }));
    }

    // 2,2,1,1 | 1,2 | 2
    // Moore voting algorithm
    // the idea is to remove minority elements using counts
    public int majorityElement(int[] nums) {
        int count = 0;
        int candidate = 0;
        for (int num : nums) {
            if (count == 0) {
                candidate = num;
            }
            if (candidate == num) {
                count++;
            } else {
                count--;
            }
        }
        return candidate;
    }
}
