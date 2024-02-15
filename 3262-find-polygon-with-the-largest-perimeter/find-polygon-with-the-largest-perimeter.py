class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        sum_of_sides = sum(nums)
        for i in range(len(nums) - 1, 1, -1):
            largest_side = nums[i]
            sum_of_sides -= largest_side
            if largest_side < sum_of_sides:
                return sum_of_sides + largest_side
        return -1