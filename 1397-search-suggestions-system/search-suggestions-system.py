class TrieNode:
    def __init__(self):
        self.children = {}      # we use
        self.end = False

class Trie:
    def __init__(self) -> None:
        self.root = TrieNode()

    def add(self, word: str) -> None:
        cur = self.root
        for char in word:
            if char not in cur.children:
                cur.children[char] = TrieNode()
            cur = cur.children[char]
        cur.end = True     

    def getTop3Prefix(self, search_word):
        cur = self.root
        res = []
        prefix = ""
        for i, char in enumerate(search_word):
            prefix += char
            if char not in cur.children:
                break
            else:
                res.append(self.getTop3Char(cur.children[char], prefix))
            cur = cur.children[char]

        while len(res) < len(search_word):
            res.append([])
        return res


    def getTop3Char(self, cur, prefix):
        top3 = []

        def dfs(node, char, prefix):
            if len(top3) == 3:
                return

            if node.end:
                top3.append(prefix)

            for letter in string.ascii_lowercase:
                if letter in node.children:
                    dfs(node.children[letter], letter, prefix + letter)

        dfs(cur, prefix[-1], prefix)
        return top3


class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        trie = Trie()
        for product in products:
            trie.add(product)
        return trie.getTop3Prefix(searchWord)