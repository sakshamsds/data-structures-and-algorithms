class TrieNode:
    def __init__(self):
        self.children = dict()
        self.words = list()

class Trie:
    def __init__(self) -> None:
        self.root = TrieNode()

    def add(self, word: str) -> None:
        cur = self.root
        for char in word:
            if char not in cur.children:
                cur.children[char] = TrieNode()
            cur = cur.children[char]
            if len(cur.words) < 3:
                cur.words.append(word)

    def find_word_by_prefix(self, prefix):
        cur = self.root
        for c in prefix:
            if c not in cur.children:
                return ''
            cur = cur.children[c]
        return cur.words

class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        trie = Trie()
        for product in products:
            trie.add(product)
        res = []
        for i in range(len(searchWord)):
            res.append(trie.find_word_by_prefix(searchWord[:i + 1]))
        return res