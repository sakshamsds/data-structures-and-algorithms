class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefixSums = collections.defaultdict(int)
        prefixSums[0] = 1
        curSum = 0
        res = 0
        for num in nums:
            curSum += num
            res += prefixSums[curSum - k]
            prefixSums[curSum] += 1
        return res