'''
100 ->
1 -> 2 -> 3 -> 4
200 ->

TC = O(n), SC = O(n)
'''

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # for every number check if it's a start of the sequence
        # if start of the sequence then expand the sequence'
        nums_set = set(nums)
        res = 0
        for num in nums:
            if num - 1 not in nums_set: # start of sequence found
                cur, cur_len = num, 0
                while cur in nums_set:
                    cur, cur_len = cur + 1, cur_len + 1
                res = max(res, cur_len)
        return res