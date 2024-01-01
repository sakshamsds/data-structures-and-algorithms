class Solution:
    def compress(self, chars: List[str]) -> int:
        array_length = 0
        l = 0
        freq = 1
        prev = chars[0]
        for r in range(1, len(chars)):
            if chars[r] == prev:
                freq += 1
            else:
                chars[l] = prev     # store char in l 
                l += 1
                if freq > 1:
                    for digit in str(freq):  # store freq in the next few elements
                        chars[l] = digit
                        l += 1
                freq = 1            # new freq is 1
            prev = chars[r]
        
        # for last char and freq
        chars[l] = prev     # store char in l 
        l += 1
        if freq > 1:
            for digit in str(freq):     # store freq in the next few elements
                chars[l] = digit
                l += 1
        return l

