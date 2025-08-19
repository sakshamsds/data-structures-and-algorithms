'''
    0   0   0   0
    1   2   3   4

    0

    0   0
'''


class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        num_zeros, res = 0, 0

        for num in nums:
            if num == 0:
                num_zeros += 1
                res += num_zeros
            else:
                num_zeros = 0

        return res
            