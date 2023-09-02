class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = False

class Trie:
    def __init__(self, words):
        self.root = TrieNode()
        for w in words:
            cur = self.root
            for c in w:
                if c not in cur.children:
                    cur.children[c] = TrieNode()
                cur = cur.children[c]
            cur.word = True

class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        # brute force solution
        # memoization
        # words = set(dictionary)     # O(1) lookup
        dp = {len(s): 0}        # base case add

        # [leet, code, leetcode]
        # s = 'ahdflkajsdfljasl;kfkjsad'

        # Prefix Tree (Trie)
        trie = Trie(dictionary).root

        # O(n * n * n)
        # start, cur pos where we add characters
        def dfs(i):
            if i in dp:
                return dp[i]

            res = 1 + dfs(i + 1)       # we skip cur char
            cur = trie
            for j in range(i, len(s)):
                if s[j] not in cur.children:
                    break
                cur = cur.children[s[j]]
                if cur.word:
                    res = min(res, dfs(j + 1))
                # if s[i:j + 1] in words:
                #     res = min(res, dfs(j + 1))
            dp[i] = res
            return res

        return dfs(0)