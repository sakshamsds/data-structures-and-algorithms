'''
0   1   3   5   5
'''

class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        return len(set(nums) - set([0]))