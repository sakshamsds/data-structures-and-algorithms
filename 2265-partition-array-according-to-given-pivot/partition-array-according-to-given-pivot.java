class Solution {
    public int[] pivotArray(int[] nums, int pivot) {
        int[] res = new int[nums.length];
        int numPivots = 0;
        int i = 0;
        for (int num : nums) {
            if (num < pivot) {
                res[i] = num;
                i++;
            } else if (num == pivot) {
                numPivots++;
            }
        }

        while (numPivots > 0) {
            res[i] = pivot;
            i++;
            numPivots--;
        }

        for (int num : nums) {
            if (num > pivot) {
                res[i] = num;
                i++;
            }
        }

        return res;
    }
}