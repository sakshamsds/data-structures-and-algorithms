class Solution:
    def decodeAtIndex(self, s: str, k: int) -> str:
        # do it in reverse

        # get size
        size = 0
        n = len(s)

        for char in s:
            if ord('a') <= ord(char) <= ord('z'):
                size += 1
            else:
                size *= int(char)

        # print(size)

        for char in s[::-1]:
            if (k == 0 or k == size) and (ord('a') <= ord(char) <= ord('z')):
                return char
            if ord('a') <= ord(char) <= ord('z'):
                size -= 1
            else:
                size /= int(char)
            k %= size

        return None

        # memory error
        # decoded_string = []
        # for char in s:
        #     if ord('a') <= ord(char) <= ord('z'):   # if alphabet
        #         decoded_string.append(char)
        #     else:
        #         decoded_string *= int(char)

        #     # print(decoded_string)
        #     if len(decoded_string) > k - 1:
        #         return decoded_string[k - 1]

        # return ""
            