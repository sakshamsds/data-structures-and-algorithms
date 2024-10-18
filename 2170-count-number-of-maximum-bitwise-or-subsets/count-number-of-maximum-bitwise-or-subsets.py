'''
a or b >= max(a, b)

3   011
2   010
1   001
5   101
7   111
'''

class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        mx_or = 0
        for num in nums:
            mx_or |= num
        
        # print(mx_or)
        @cache
        def backtrack(i, cur_or):
            if cur_or == mx_or:
                return 2 ** (len(nums) - i)
            
            if i == len(nums):
                return 0

            return backtrack(i + 1, cur_or) + backtrack(i + 1, cur_or | nums[i])

        return backtrack(0, 0)