class TrieNode:
    def __init__(self):
        self.children = {}
        self.start = 0
        self.end = 0

class Trie:
    def __init__(self, ):
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
        cur = self._walk(word)
        return cur.end if cur else 0

    def countWordsStartingWith(self, word: str) -> int:
        cur = self._walk(word)
        return cur.start if cur else 0

    def erase(self, word: str) -> None:
        parent = self.root
        for c in word:
            child = parent.children[c]
            child.start -= 1
            if child.start == 0:
                parent.children.pop(c)
                return
            parent = child
        child.end -= 1

    def _walk(self, word):
        cur = self.root
        for c in word:
            if c not in cur.children:
                return None
            cur = cur.children[c]
        return cur


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.countWordsEqualTo(word)
# param_3 = obj.countWordsStartingWith(prefix)
# obj.erase(word)
