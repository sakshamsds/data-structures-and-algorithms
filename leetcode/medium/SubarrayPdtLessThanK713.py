
from typing import List

class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k == 0:
            return 0
        
        count = 0
        left = 0
        pdt = 1

        for right in range(len(nums)):
            pdt *= nums[right]

            while pdt >= k and left <= right:
                pdt /= nums[left]
                left += 1

            count += right - left + 1

        return count
        

        # # brute force
        # for i in range(len(nums)):
        #     pdt = nums[i]
        #     if pdt < k:
        #         count += 1
        #     for j in range(i+1, len(nums)):
        #         pdt *= nums[j]
        #         if pdt < k:
        #             count += 1
        #         else:
        #             break
        # return count

    
Solution().numSubarrayProductLessThanK([1, 1, 1], 1)
# Solution().numSubarrayProductLessThanK([10, 5, 2, 6], 100)
    