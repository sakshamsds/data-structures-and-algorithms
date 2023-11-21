class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(s) < len(p):
            return []

        # encode p
        p_encoded = [0] * 26
        for char in p:
            p_encoded[ord(char) - ord('a')] += 1
        # print(p_encoded)

        # use sliding window to match
        res = []
        s_encoded = [0] * 26
        for i in range(len(p) - 1):     # encode starting substring
            s_encoded[ord(s[i]) - ord('a')] += 1

        for r in range(len(p) - 1, len(s)):
            s_encoded[ord(s[r]) - ord('a')] += 1    # add cur char to encoding
            if s_encoded == p_encoded:      # match
                res.append(r - len(p) + 1)
            s_encoded[ord(s[r - len(p) + 1]) - ord('a')] -= 1  # remvoe i - k char from the encoding

        return res