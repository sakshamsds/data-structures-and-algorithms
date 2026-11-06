class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        # match every characters
        prefix = []
        for i, c in enumerate(strs[0]):
            for word in strs:
                if len(word) == i or word[i] != c:
                    return ''.join(prefix)
            prefix.append(c)
        return ''.join(prefix)
                