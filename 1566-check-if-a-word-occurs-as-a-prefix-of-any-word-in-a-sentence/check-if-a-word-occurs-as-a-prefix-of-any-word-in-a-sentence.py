class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        # prefix matching
        for i, word in enumerate(sentence.split()):
            if len(word) < len(searchWord):
                continue
            if word[:len(searchWord)] == searchWord:
                return i + 1
        return -1