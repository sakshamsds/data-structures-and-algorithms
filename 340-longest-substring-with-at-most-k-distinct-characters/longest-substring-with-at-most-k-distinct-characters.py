class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        n = len(s)
        max_size = 0
        counter = collections.Counter()
        
        left = 0
        for right in range(n):
            counter[s[right]] += 1
            
            if len(counter) > k:        # if valid
                counter[s[left]] -= 1
                if not counter[s[left]]:
                    counter.pop(s[left])
                left += 1

            max_size = max(max_size, right - left + 1)
                    
        return max_size