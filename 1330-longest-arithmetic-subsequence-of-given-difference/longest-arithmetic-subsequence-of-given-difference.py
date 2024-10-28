class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        prev = {}
        longest = 1
        for num in arr:
            if num - difference in prev:
                prev[num] = 1 + prev[num - difference]
                longest = max(longest, prev[num])
            else:
                prev[num] = 1
        return longest

        
