class Solution:
    def countSegments(self, s: str) -> int:
        segments = 0
        for i in range(len(s)):
            if s[i] != ' ' and (i==0 or s[i-1] == ' '):
                segments += 1
        return segments
    
        # segments = 0
        # i = 0
        # while i < len(s):
        #     if s[i] != " ":
        #         segments += 1
        #         while i < len(s) and s[i] != " ":
        #             i += 1
        #     i += 1
        # return segments

