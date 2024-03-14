class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        # subarray sum == k
        prefixes = collections.defaultdict(int)
        prefixes[0] = 1
        cur, res = 0, 0
        for num in nums:
            cur += num
            res += prefixes[cur - goal]
            prefixes[cur] += 1
        return res