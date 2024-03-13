class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        cache = collections.defaultdict(int)
        cache[0] = 1
        prefix, res = 0, 0
        for num in nums:
            prefix += num
            res += cache[prefix - k]
            cache[prefix] += 1
        return res