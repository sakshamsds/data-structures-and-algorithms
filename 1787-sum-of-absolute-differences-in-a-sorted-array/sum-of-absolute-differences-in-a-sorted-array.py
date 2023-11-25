class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        prefixSum = [nums[0]]
        for i in range(1, len(nums)):
            prefixSum.append(prefixSum[i - 1] + nums[i])
        # print(prefixSum)

        n, totalSum = len(nums), prefixSum[-1]
        res = []
        for i, num in enumerate(nums):
            leftSum = prefixSum[i] - num
            rightSum = totalSum - prefixSum[i]
            total_diff = (i * num - leftSum) + (rightSum - (n - i - 1) * num)
            # total_diff = (leftSize * num - leftSum) + \
            #              (rightSum - rightSize * num)
            res.append(total_diff)

        return res
