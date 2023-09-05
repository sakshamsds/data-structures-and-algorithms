# build a trie

class TrieNode:
    def __init__(self) -> None:
        self.children = dict()
        self.end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
        self.root.end = True

    def add_word(self, word) -> None:
        cur = self.root
        for char in word:
            if char not in cur.children:
                cur.children[char] = TrieNode()
            cur = cur.children[char]
        cur.end = True

    def get_longest(self) -> str:
        self.res = ""
        def dfs(node, prefix):
            for child in node.children:
                # go deep only if there is an end here
                if node.end:
                    dfs(node.children[child], prefix + child)
            if node.end:
                # print(prefix)
                if len(prefix) > len(self.res) or (len(prefix) == len(self.res) and prefix < self.res):
                    self.res = prefix
            return

        dfs(self.root, "")
        return self.res


class Solution:
    def longestWord(self, words: List[str]) -> str:
        trie = Trie()
        for word in words:
            trie.add_word(word)
        return trie.get_longest()


        