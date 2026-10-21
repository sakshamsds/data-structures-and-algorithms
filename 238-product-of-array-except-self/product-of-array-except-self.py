'''
                    1   2   3   4
    left pdt        1   1   2   6
    right pdt       24  12  4   1    
'''


class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        right_pdt = [1]
        for num in nums[::-1]:
            right_pdt.append(right_pdt[-1] * num)
        right_pdt.reverse()

        left_pdt = 1
        res = []
        for i, num in enumerate(nums):   
            res.append(left_pdt * right_pdt[i + 1])
            left_pdt *= num
        return res
