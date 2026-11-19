class TrieNode:
    def __init__(self):
        self.children = dict()
        self.end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def add(self, word):
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.end = True
    
    def match(self, word, startIdx):
        cur = self.root
        nxtIdxs = []
        for i in range(startIdx, len(word)):
            c = word[i]
            if c not in cur.children:
                break
            if cur.children[c].end:     # if a word ends here
                nxtIdxs.append(i + 1)
            cur = cur.children[c]
        return nxtIdxs

class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        trie = Trie()
        for word in dictionary:
            trie.add(word)
        
        cache = {}

        def dfs(i):
            if i >= len(s):
                return 0
            if i in cache:
                return cache[i]

            # skip cur
            left = 1 + dfs(i + 1)

            # don't skip cur
            nxtIdxs = trie.match(s, i)
            for j in nxtIdxs:
                left = min(left, dfs(j))

            cache[i] = left
            return left

        return dfs(0)