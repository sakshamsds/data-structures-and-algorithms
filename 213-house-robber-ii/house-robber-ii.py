class Solution:
    def rob(self, nums: list[int]) -> int:
        def maxRob(houses):
            r, nr = 0, 0
            for h in houses:
                r, nr = h + nr, max(r, nr)
            return max(r, nr)

        return max(nums[0], maxRob(nums[1:]), maxRob(nums[:-1]))