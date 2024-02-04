class Solution:
    def returnToBoundaryCount(self, nums: List[int]) -> int:
        cur_sum = 0
        res = 0
        for num in nums:
            cur_sum += num
            if cur_sum == 0:
                res += 1
        return res
