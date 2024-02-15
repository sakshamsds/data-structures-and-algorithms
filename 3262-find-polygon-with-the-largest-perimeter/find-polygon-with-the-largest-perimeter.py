class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        sum_of_sides = nums[0] + nums[1]
        max_perimeter = -1
        for i in range(2, len(nums)):
            largest_side = nums[i]
            if largest_side < sum_of_sides:
                max_perimeter = max(max_perimeter, sum_of_sides + largest_side)
            sum_of_sides += largest_side
        return max_perimeter