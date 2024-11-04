class Solution:
    def compressedString(self, word: str) -> str:
        comp = []    
        prev, freq = '', 0
        for c in word:
            if c == prev:
                if freq == 9:
                    comp.append('9')
                    comp.append(c)
                    freq = 0
                freq += 1
            else:
                comp.append(str(freq))
                comp.append(prev)
                freq = 1
            prev = c

        comp.append(str(freq))
        comp.append(prev)
        return ''.join(comp)[1:]

        
