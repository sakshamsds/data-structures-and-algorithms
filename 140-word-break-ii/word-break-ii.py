class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def add(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.end = True

    def search(self, s, i) -> int:
        cur = self.root
        nextPtrs = []
        while i < len(s):
            # print(s[i], cur.children)
            if s[i] not in cur.children:
                break
            cur = cur.children[s[i]]
            if cur.end:
                nextPtrs.append(i + 1)
            i += 1
        return nextPtrs

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        trie = Trie()
        for word in wordDict:
            trie.add(word)
        # print(trie.search(s, 0))

        res = []
        subset = []

        def dfs(i):
            if i == len(s):
                res.append(' '.join(subset.copy()))
                return

            nextPtrs = trie.search(s, i)
            for j in nextPtrs:
                subset.append(s[i:j])
                dfs(j)
                subset.pop()

        dfs(0)
        return res
        