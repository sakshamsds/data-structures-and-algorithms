class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        res = [0] * len(nums)
        e_i, o_i = 0, 1
        for num in nums:
            if num > 0:
                res[e_i] = num
                e_i += 2
            else:
                res[o_i] = num
                o_i += 2
        return res