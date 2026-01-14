class TrieNode:
    def __init__(self):
        self.map = {}
        self.end = False


class Trie:
    def __init__(self):
        self.node = TrieNode()
        
    def add(self, word):
        cur = self.node
        for c in word:
            if c not in cur.map:
                cur.map[c] = TrieNode()
            cur = cur.map[c]
        cur.end = True


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        m, n = len(board), len(board[0])
        trie = Trie()
        for word in words:
            trie.add(word)
        # print(trie.node.map.keys())

        visited = set()
        def dfs(i, j, prefix, cur):
            if i < 0 or j < 0 or i >= m or j >= n or (i, j) in visited:
                return

            visited.add((i, j))
            c = board[i][j]
            if c in cur.map:
                new_prefix = prefix + c
                if cur.map[c].end:
                    found.add(new_prefix)
                dfs(i + 1, j, new_prefix, cur.map[c])
                dfs(i, j + 1, new_prefix, cur.map[c])
                dfs(i - 1, j, new_prefix, cur.map[c])
                dfs(i, j - 1, new_prefix, cur.map[c])

            visited.remove((i, j))
            return

        found = set()
        for r in range(m):
            for c in range(n):
                dfs(r, c, "", trie.node)

        return list(found)        