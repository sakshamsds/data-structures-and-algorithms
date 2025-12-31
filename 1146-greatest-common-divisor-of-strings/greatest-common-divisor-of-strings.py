class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        len1, len2 = len(str1), len(str2)

        def isDivisor(end):
            if len1 % end != 0 or len2 % end != 0:
                return False
            freq1, freq2 = len1 // end, len2 // end
            prefix = str1[:end]
            return prefix * freq1 == str1 and prefix * freq2 == str2

        for end in range(min(len1, len2), 0, -1):
            if isDivisor(end):
                return str1[:end]

        return ""