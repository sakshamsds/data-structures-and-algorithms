class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:

        def isGood(word):
            charsDict = collections.Counter(chars)
            for c in word:
                if charsDict[c] == 0:
                    return False
                else:
                    charsDict[c] -= 1
            return True
                
        res = 0
        for word in words:
            if isGood(word):
                res += len(word)

        return res