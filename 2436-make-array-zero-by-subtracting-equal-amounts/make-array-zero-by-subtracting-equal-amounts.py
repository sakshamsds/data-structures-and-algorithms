'''
0   1   3   5   5
'''

class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        uniques = set(nums)
        if 0 in uniques:
            return len(uniques) - 1
        else:
            return len(uniques)