class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split(' ')[::-1]
        res = []
        for word in words:
            if word != '':
                res.append(word)
        return ' '.join(res).strip()