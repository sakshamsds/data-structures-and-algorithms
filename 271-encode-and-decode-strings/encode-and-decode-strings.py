'''
    neet code
    4#neet4#code
'''

class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        encoded = []
        for word in strs:
            encoded.append(str(len(word)) + "#" + word)
        return ''.join(encoded)

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        decoded = []
        i = 0
        while i < len(s):
            digits = ""
            while s[i] != '#':
                digits += s[i]
                i += 1
            i += 1
            length = int(digits)
            decoded.append(s[i:i+length])
            i += length
        return decoded
        


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))