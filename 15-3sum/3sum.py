'''
    -4  -1  -1  0   1   2
'''

class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()

        # fix first point
        prev = float(-inf)
        res = set()

        for i in range(len(nums)):
            l, r = i + 1, len(nums) - 1
            while l < r:
                curSum = nums[i] + nums[l] + nums[r]
                if curSum == 0:
                    res.add(tuple(sorted((nums[i], nums[l], nums[r]))))
                    l += 1
                    r -= 1
                elif curSum > 0:
                    r -= 1
                else:
                    l += 1
        
        return [list(v) for v in res]