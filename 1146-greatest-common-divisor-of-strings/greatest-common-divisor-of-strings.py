class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # decide divisor using prefix, long to short
        len1, len2 = len(str1), len(str2)

        for prefix_len in range(min(len1, len2), 0, -1):
            prefix = str1[:prefix_len]

            # check 1
            if len1 % prefix_len != 0 or len2 % prefix_len != 0:
                continue
            
            # check 2
            q1, q2 = len1 // prefix_len, len2 // prefix_len
            if prefix * q1 != str1 or prefix * q2 != str2:
                continue

            return prefix

        return ""
