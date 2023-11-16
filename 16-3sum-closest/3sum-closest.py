class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        closest_sum = float('inf')

        n = len(nums)
        for i in range(n - 2):
            # skip duplicates
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            l, r = i + 1, n - 1
            while l < r:
                sum_3 = nums[i] + nums[l] + nums[r]
                if sum_3 == target:     # early termination
                    return sum_3
                if abs(target - sum_3) < abs(target - closest_sum):
                    closest_sum = sum_3

                if sum_3 > target:
                    r -= 1
                else:
                    l += 1

        return closest_sum
