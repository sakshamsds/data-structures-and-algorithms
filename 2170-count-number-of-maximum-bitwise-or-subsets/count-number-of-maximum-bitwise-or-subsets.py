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

        def backtrack(i, cur_or):
            if i == len(nums):
                return 1 if cur_or == mx_or else 0

            cnt = backtrack(i + 1, cur_or)
            cnt += backtrack(i + 1, cur_or | nums[i])
            # cnt = 0
            # for j in range(i, len(nums)):
                # cnt += backtrack(j + 1, cur_or | nums[j])

            return cnt

        return backtrack(0, 0)