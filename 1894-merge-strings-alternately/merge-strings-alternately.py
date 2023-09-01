class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        
        res = []
        n, m = len(word1), len(word2)
        i, j = 0, 0
        add_word1 = True

        while i < n and j < m:
            if add_word1:
                res.append(word1[i])
                i += 1
            else:
                res.append(word2[j])
                j += 1
            add_word1 = not add_word1

        if i < n:
            res.append(word1[i:])
        
        if j < m:
            res.append(word2[j:])

        return ''.join(res)

            