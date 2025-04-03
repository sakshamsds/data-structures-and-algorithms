class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        n = len(nums)
        leftMax = [0] * n
        rightMax = [0] * n
        for i in range(1, n - 1):
            leftMax[i] = max(leftMax[i - 1], nums[i - 1])
            rightMax[n - 1 - i] = max(rightMax[n - i], nums[n - i])

        max_triplet = 0
        for j in range(1, n - 1):
            max_triplet = max(max_triplet, (leftMax[j] - nums[j]) * rightMax[j])

        return max_triplet
