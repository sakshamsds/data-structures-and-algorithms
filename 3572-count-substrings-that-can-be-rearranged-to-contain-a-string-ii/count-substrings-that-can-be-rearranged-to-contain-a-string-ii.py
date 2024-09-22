class Solution:
    def validSubstringCount(self, word1: str, word2: str) -> int:
        w1_freq = [0] * 26
        w2_freq = [0] * 26
        for c in word2:
            w2_freq[ord(c) - 97] += 1

        rem_matches = len(set(word2))
        cnt, r = 0, 0
        for l in range(len(word1)):
            while r < len(word1) and rem_matches > 0:
                idx = ord(word1[r]) - 97
                w1_freq[idx] += 1    
                if w1_freq[idx] == w2_freq[idx]:
                    rem_matches -= 1
                r += 1

            if rem_matches == 0:
                cnt += len(word1) - r + 1

            idx = ord(word1[l]) - 97
            w1_freq[idx] -= 1  
            # if w1_freq[idx] < w2_freq[idx]:
            if w1_freq[idx] == w2_freq[idx] - 1:
                rem_matches += 1         
            
        return cnt
            