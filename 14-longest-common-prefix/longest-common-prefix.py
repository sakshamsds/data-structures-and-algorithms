class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ""
        for i in range(len(strs[0])):
            prefix = strs[0][:i + 1]
            for word in strs:
                if len(word) < i + 1 or word[:i + 1] != prefix:
                    return prefix[:-1]
        return prefix