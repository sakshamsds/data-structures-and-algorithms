'''
leetcode 
dfs(0) -> matches with leet -> dfs(4) -> matches with code -> dfs(8) = True
'''


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        cache = {len(s): True}
        
        def dfs(idx):
            if idx in cache:    # already computed the subproblem
                return cache[idx]

            for word in wordDict:
                if idx + len(word) <= len(s) and s[idx:idx + len(word)] == word:
                    if dfs(idx + len(word)):
                        cache[idx] = True
                        return True

            cache[idx] = False
            return False
        
        return dfs(0)
