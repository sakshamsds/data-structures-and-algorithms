class Solution:
    def smallestBalancedIndex(self, nums: list[int]) -> int:
        leftSum = sum(nums)
        rightPdt = 1

        for i in range(len(nums) - 1, -1, -1):
            leftSum -= nums[i]
            if leftSum == rightPdt:
                return i
            elif leftSum < rightPdt:
                break
            rightPdt *= nums[i]

        return -1