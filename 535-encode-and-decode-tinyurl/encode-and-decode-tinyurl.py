class Codec:

    def __init__(self):
        self.longToTiny = {}
        self.tinyToLong = {}
        self.baseUrl = "http://tinyUrl.com/"

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        if longUrl not in self.longToTiny:
            code = self.baseUrl + self.getCode(len(self.longToTiny))
            self.longToTiny[longUrl] = code
            self.tinyToLong[code] = longUrl
        return self.longToTiny[longUrl]

    def getCode(self, num):
        if num == 0:
            return '0'
        res = []
        while num > 0:
            digit = num % 62
            if digit < 10:
                res.append(str(digit))
            elif digit < 36:
                res.append(chr(digit - 10 + ord("A")))
            else:
                res.append(chr(digit - 36 + ord("a")))
            num //= 62
        return ''.join(res)

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        # code = shortUrl.split('/')[-1]
        code = shortUrl.rpartition('/')[2]
        return self.tinyToLong[shortUrl]
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))
