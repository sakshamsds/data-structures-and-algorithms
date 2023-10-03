class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        freq_map = defaultdict(int)
        for num in nums:
            freq_map[num] += 1

        res = 0
        for num, freq in freq_map.items():
            if freq > 1:
                res += freq * (freq - 1) // 2
            
        return res