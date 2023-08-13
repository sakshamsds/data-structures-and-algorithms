"""
You are given a 0-indexed integer array nums and an integer x.

Find the minimum absolute difference between two elements in the array that are at least x indices apart.

In other words, find two indices i and j such that abs(i - j) >= x and abs(nums[i] - nums[j]) is minimized.

Return an integer denoting the minimum absolute difference between two elements that are at least x indices apart.
"""

def minAbsoluteDifference(nums, x):
    nums.sort()
    n = len(nums)
    min_diff = float('inf')
    
    for i in range(n - x):
        min_diff = min(min_diff, nums[i + x] - nums[i])
    
    return min_diff

# Example usage
nums = [4,3,2,4]
# nums = [1, 3, 7, 8, 10]
x = 2
result = minAbsoluteDifference(nums, x)
print(result)  # Output: 1
