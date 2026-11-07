class Solution:
    def gcdOfStrings(self, s1: str, s2: str) -> str:
        if s1 + s2 != s2 + s1:
            return ""
        
        def gcd(a, b):
            if b == 0:
                return a
            return gcd(b, a % b)

        l1, l2 = len(s1), len(s2)      
        g = gcd(max(l1, l2), min(l1, l2))
        return s1[:g]