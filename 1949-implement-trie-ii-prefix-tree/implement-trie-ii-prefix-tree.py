class TrieNode:
    def __init__(self):
        self.children = {}
        self.start = 0
        self.end = 0


class Trie:
    def __init__(
        self,
    ):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
            cur.start += 1
        cur.end += 1

    def countWordsEqualTo(self, word: str) -> int:
        cur = self.root
        for c in word:
            if c not in cur.children:
                return 0
            cur = cur.children[c]
        return cur.end

    def countWordsStartingWith(self, word: str) -> int:
        cur = self.root
        for c in word:
            if c not in cur.children:
                return 0
            cur = cur.children[c]
        return cur.start

    def erase(self, word: str) -> None:
        cur = self.root
        for c in word:
            cur = cur.children[c]
            cur.start -= 1
        cur.end -= 1


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.countWordsEqualTo(word)
# param_3 = obj.countWordsStartingWith(prefix)
# obj.erase(word)
