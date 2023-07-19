from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        # O(nlogn)
        # nums.sort()
        # return nums[len(nums)//2]

        # O(n)
        # freq_map = {}
        # res, max_count = 0, 0

        # for n in nums:
        #     freq_map[n] = 1 + freq_map.get(n, 0)
        #     res = n if freq_map[n] > max_count else res
        #     max_count = max(freq_map[n], max_count)
        # return res

        # Moore Voting algorithm
        # Boyer-Moore algorithm

        res, count = 0, 0
        for n in nums:
            if count == 0:
                res = n
            count += (1 if n == res else -1)

        return res

