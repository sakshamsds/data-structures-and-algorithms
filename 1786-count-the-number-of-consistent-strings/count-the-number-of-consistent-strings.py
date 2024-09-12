class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allowed = set(allowed)
        res = 0
        for word in words:
            consistent = True
            for c in word:
                if c not in allowed:
                    consistent = 0
                    break
            res += consistent
        return res