class Solution:
    def compress(self, chars: List[str]) -> int:
        l, freq = 0, 1
        prev = chars[0]
        for r in range(1, len(chars)):
            if chars[r] == prev:
                freq += 1
            else:
                l = self.populateChars(chars, freq, l, prev)
                freq = 1            # new freq is 1
            prev = chars[r]
        
        # for last char and freq
        l = self.populateChars(chars, freq, l, prev)
        return l

    def populateChars(self, chars, freq, idx, prev):
        chars[idx] = prev     # store char in l 
        idx += 1
        if freq > 1:
            for digit in str(freq):     # store freq in the next few elements
                chars[idx] = digit
                idx += 1
        return idx

