class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        num1, num2 = max(nums[0], nums[1]), min(nums[0], nums[1])

        for i in range(2, len(nums)):
            num = nums[i]
            if num > num1:
                num1, num2 = num, num1
            elif num2 < num <= num1:
                num2 = num

        return (num1 - 1) * (num2 - 1)
                