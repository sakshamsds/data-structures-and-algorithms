/**
    1   1   2
 */


class Solution {
    public int maximumElementAfterDecrementingAndRearranging(int[] arr) {
        // what the element should be,
        // what it actually is
        Arrays.sort(arr);
        int expected = 1;
        for (int num : arr) {
            if (num >= expected) {
                expected += 1;
            } else {
                expected = num + 1;
            }
        }
        return expected - 1;
    }
}