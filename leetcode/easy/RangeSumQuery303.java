package easy;

public class RangeSumQuery303 {
    public static void main(String[] args) {

    }

}

class NumArray {

    // prefix sum

    private int[] prefixSum;

    public NumArray(int[] nums) {
        for (int i = 1; i < nums.length; i++) {
            nums[i] += nums[i - 1];
        }
        prefixSum=nums;
    }

    public int sumRange(int left, int right) {
        if(left==0){
            return prefixSum[right];
        }
        return prefixSum[right] - prefixSum[left-1];
    }
}