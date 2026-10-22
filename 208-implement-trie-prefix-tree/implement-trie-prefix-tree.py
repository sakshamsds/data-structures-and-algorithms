class TrieNode:
	def __init__(self):
		self.map = {}
		self.word_end = False

class Trie:
	
	def __init__(self):
		self.root = TrieNode()

	def  insert(self, word: str) -> None:
		cur = self.root
		for c in word:
			if c not in cur.map:
				cur.map[c] = TrieNode()
			cur = cur.map[c]
		cur.word_end = True
		
	def searchHelper(self, word):		# return prefix, word
		cur = self.root
		for c in word:
			if c not in cur.map:
				return False, False
			cur = cur.map[c]
		return True, cur.word_end

	def search(self, word: str) -> bool:
		return self.searchHelper(word)[1]

	def startsWith(self, prefix: str) -> bool:
		return self.searchHelper(prefix)[0]



# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)