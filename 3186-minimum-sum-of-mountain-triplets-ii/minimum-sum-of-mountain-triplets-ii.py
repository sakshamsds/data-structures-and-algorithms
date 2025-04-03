class Solution:
    def minimumSum(self, nums: List[int]) -> int:
        n = len(nums)
        leftMin = [nums[0]] * len(nums)
        rightMin = [nums[-1]] * len(nums)

        for i in range(1, n - 1):
            leftMin[i] = min(leftMin[i - 1], nums[i - 1])
            rightMin[n - 1 - i] = min(rightMin[n - i], nums[n - i])

        # print(leftMin)
        # print(rightMin)

        min_triplet = float('inf')
        
        for i in range(1, n - 1):
            if leftMin[i] < nums[i] and rightMin[i] < nums[i]:
                min_triplet = min(min_triplet, nums[i] + leftMin[i] + rightMin[i])

        return -1 if min_triplet == float('inf') else min_triplet