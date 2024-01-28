class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sums = collections.defaultdict(int)
        prefix_sums[0] = 1          # base condition
        cur_sum, res = 0, 0
        for num in nums:
            cur_sum += num
            res += prefix_sums[cur_sum - k]
            prefix_sums[cur_sum] += 1
        return res