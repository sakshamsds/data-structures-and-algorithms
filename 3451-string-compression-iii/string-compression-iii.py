class Solution:
    def compressedString(self, word: str) -> str:
        res = []    
        prev, freq = '', 0
        for c in word:
            if c == prev:
                freq += 1
            else:
                res.append(('9' + prev) * (freq // 9))
                rem = freq % 9
                if rem > 0:
                    res.append(str(freq % 9) + prev)
                freq = 1
            prev = c

        res.append(('9' + prev) * (freq // 9))
        rem = freq % 9
        if rem > 0:
            res.append(str(freq % 9) + prev)
        return ''.join(res)

        
