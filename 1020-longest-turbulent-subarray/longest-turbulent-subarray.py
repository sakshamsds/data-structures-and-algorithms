'''
        9   4   2
size        2   
comp        -1  -1
'''


class Solution:
    def maxTurbulenceSize(self, nums: List[int]) -> int:
        mx_size = 1
        prev, cur_size = None, 1

        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                if prev != 'decrement':
                    cur_size = 2
                else:
                    cur_size += 1
                prev = 'increment'
            elif nums[i] < nums[i - 1]:
                if prev != 'increment':
                    cur_size = 2
                else:
                    cur_size += 1
                prev = 'decrement'
            else:
                prev, cur_size = None, 1
            mx_size = max(mx_size, cur_size)

        return mx_size