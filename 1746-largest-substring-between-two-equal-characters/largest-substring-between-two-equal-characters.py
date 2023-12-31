class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        start_indices = dict()        
        longest = -1
        for i, char in enumerate(s):
            if char in start_indices:
                longest = max(longest, i - start_indices[char] - 1)
            else:
                start_indices[char] = i
        return longest