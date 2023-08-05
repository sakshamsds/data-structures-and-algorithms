from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
# https://leetcode.com/problems/maximum-product-subarray/solutions/1608907/python3-dynamic-programming-explained/

        # kadane's algorithm
        # dp
        best_pdt = nums[0]
        cur_max_pdt = 1
        cur_min_pdt = 1
        for num in nums:
            # print(cur_max_pdt, cur_min_pdt)
            vals = (num, num * cur_max_pdt, num * cur_min_pdt)
            cur_max_pdt = max(vals)
            cur_min_pdt = min(vals)
            best_pdt = max(cur_max_pdt, best_pdt)
        return best_pdt

print(Solution().maxProduct([-4,-3,-2]))