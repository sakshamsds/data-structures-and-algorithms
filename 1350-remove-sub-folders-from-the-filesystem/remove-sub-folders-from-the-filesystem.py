class TrieNode:
    def __init__(self):
        self.mp = {}
        self.end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def add(self, directory):
        cur = self.root
        for folder in directory:
            if not cur.end:
                if folder not in cur.mp:
                    cur.mp[folder] = TrieNode()
                cur = cur.mp[folder] 
        cur.end = True
        cur.mp = {}

    def getFolders(self):
        res, cur = [], ['.']
        def backtrack(node):
            if node.end:
                res.append('/'.join(cur)[1:])
            for folder, subNode in node.mp.items():
                cur.append(folder)
                backtrack(subNode)
                cur.pop()
        backtrack(self.root)
        return res


class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        trie = Trie()
        for f in folder:
            trie.add(f.split('/')[1:])
        return trie.getFolders()