class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        res = []
        for word1 in words:
            for word2 in words:
                if word1 != word2 and word1 in word2:
                    res.append(word1)
                    break
        return res