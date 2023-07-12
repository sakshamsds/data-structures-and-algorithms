from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1] * n
        
        prefix_pdt = 1
        for i in range(n):
            res[i] = prefix_pdt
            prefix_pdt *= nums[i]

        postfix_pdt = 1
        for i in range(n - 1, -1, -1):
            res[i] *= postfix_pdt
            postfix_pdt *= nums[i]

        return res
    
        # O(N), O(N)
        # prefix_pdts = []
        # suffix_pdts = []

        # prefix_pdt = 1
        # suffix_pdt = 1

        # n = len(nums)

        # for i in range(n):
        #     prefix_pdt *= nums[i]
        #     suffix_pdt *= nums[n - i - 1]
        #     prefix_pdts.append(prefix_pdt)
        #     suffix_pdts.append(suffix_pdt)

        # # print(prefix_pdts)
        # # print(suffix_pdts)

        # res = [suffix_pdts[n - 2]]

        # for i in range(1, n - 1):
        #     res.append(prefix_pdts[i-1] * suffix_pdts[n - i - 2])
        # res.append(prefix_pdts[n - 2])

        # return res

print(Solution().productExceptSelf([1,2]))
print(Solution().productExceptSelf([1,2,3,4]))