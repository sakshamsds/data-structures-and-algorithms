'''
look for num - k, num + k in the lookup store
calculate subarray sum using prefixes
store the lowest prefix sub before current element
'''

class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        lowestPrefixSum = {}      # num, lowest prefix sum before cur element

        MIN_VAL, MAX_VAL = -float('inf'), float('inf')
        maxSum, curSum = MIN_VAL, 0
        for num in nums:
            lowestPrefixSum[num] = min(lowestPrefixSum.get(num, MAX_VAL), curSum)
            curSum += num
            maxSum = max(
                maxSum,
                curSum - lowestPrefixSum.get(num - k, MAX_VAL), 
                curSum - lowestPrefixSum.get(num + k, MAX_VAL)
            )

        return 0 if maxSum == MIN_VAL else maxSum