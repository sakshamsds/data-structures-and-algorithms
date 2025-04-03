class Solution:
    def sumOfBeauties(self, nums: List[int]) -> int:
        points = [0] * len(nums)

        left_max = nums[0]
        for i in range(1, len(nums) - 1):
            if nums[i] > left_max:
                points[i] = 2
            elif nums[i] > nums[i - 1]:
                points[i] = 1
            left_max = max(left_max, nums[i])

        right_min = nums[-1]
        for i in range(len(nums) - 2, 0, -1):
            if points[i] != 0:
                if nums[i] >= nums[i + 1]:
                    points[i] = 0
                elif nums[i] >= right_min:
                    points[i] = 1
            right_min = min(right_min, nums[i])

        return sum(points)