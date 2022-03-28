package easy;

import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;
import java.util.Stack;

// https://leetcode.com/problems/next-greater-element-i/
// 496. Next Greater Element I

public class NextGreater496 {

    public static void main(String[] args) {
        int[] nums1 = { 4, 1, 2 };
        int[] nums2 = { 1, 3, 4, 2 };
        System.out.println(Arrays.toString(nextGreaterElement(nums1, nums2)));
    }

    public static int[] nextGreaterElement(int[] nums1, int[] nums2) {

        // O(N) using a stack, worst case is O(N^2)
        Map<Integer, Integer> storeageMap = new HashMap<>();
        Stack<Integer> compStack = new Stack<>();

        for (int num : nums2) {

            while (!compStack.isEmpty() && compStack.peek() < num) {
                storeageMap.put(compStack.pop(), num);
            }
            compStack.push(num);

        }

        // System.out.println(storeageMap.toString());
        // System.out.println(compStack.toString());

        for (int i=0; i<nums1.length; i++) {
            nums1[i] = storeageMap.getOrDefault(nums1[i], -1);
        }

        // O(N^2)

        // for (int i = 0; i < nums1.length; i++) {
        // boolean numFound = false;
        // int nextGreater = -1;

        // for (int j = 0; j < nums2.length; j++) {
        // if (nums2[j] == nums1[i]) {
        // numFound = true;
        // } else if (numFound && nums2[j] > nums1[i]) {
        // // look for next greatest elemnt
        // nextGreater = nums2[j];
        // break;
        // }
        // }

        // nums1[i] = nextGreater;
        // }

        return nums1;
    }
}
