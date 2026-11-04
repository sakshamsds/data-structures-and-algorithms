'''
            b   b   b   a   b
        0   0   0   0   0   0
    b   0   1   1   1   1   1
    a   0   1   1   1   2   2
    b   
    b   
    b   
'''

class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        return self.longestCommonSubsequence(s, s[::-1])
        
    def longestCommonSubsequence(self, s1: str, s2: str) -> int:
        prevDp = [0] * (len(s2) + 1)
        for r in range(len(s1)):
            newDp = [0] * (len(s2) + 1)
            for c in range(len(s2)):
                increment = 1 if s1[r] == s2[c] else 0
                newDp[c + 1] = max(
                    newDp[c],
                    prevDp[c + 1],
                    prevDp[c] + increment
                )
            prevDp = newDp
        return prevDp[-1]