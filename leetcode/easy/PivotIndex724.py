from typing import List

# https://leetcode.com/problems/find-pivot-index/

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums)
        leftSum = 0
        rightSum = total

        for i in range(len(nums)):
            rightSum -= nums[i]
            if leftSum == rightSum:
                return i
            leftSum += nums[i]

        return -1

inst = Solution()
print(inst.pivotIndex([1, 7, 3, 6, 5, 6]))
print(inst.pivotIndex([1, 2, 3]))
print(inst.pivotIndex([2, 1, -1]))
print(inst.pivotIndex([-1, -1, -1, 1, 1, 1]))
