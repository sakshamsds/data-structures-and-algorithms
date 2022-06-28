
# https://leetcode.com/problems/running-sum-of-1d-array/
# 1480. Running Sum of 1d Array

def runningSum(nums: list[int]) -> list[int]:
    for i in range(1, len(nums)):
        nums[i] += nums[i-1]
    return nums


print(runningSum([1, 2, 3, 4]))
