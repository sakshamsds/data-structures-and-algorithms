class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int largestSum = INT_MIN;
        int currentSum = -1;

        for (auto num: nums) {
            currentSum = max(num, num + currentSum);
            largestSum = max(currentSum, largestSum);
        }
        return largestSum;
    }
};