'''
    1   2   3   4
    24  24  12  4   1
            6
    24  12  8   6

'''

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1]
        rightPdt = 1
        n = len(nums)
        for i in range(n - 1, 0, -1):
            rightPdt *= nums[i]
            res.append(rightPdt)

        res = res[::-1]
        leftPdt = 1
        for i in range(n):
            res[i] *= leftPdt
            leftPdt *= nums[i]

        return res