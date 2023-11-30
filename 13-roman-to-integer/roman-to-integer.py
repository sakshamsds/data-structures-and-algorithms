class Solution:
    def romanToInt(self, s: str) -> int:
        valueDict = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        
        res = 0
        for i in range(len(s)):
            if i < len(s) - 1 and valueDict[s[i]] < valueDict[s[i + 1]]:
                res -= valueDict[s[i]]
            else:
                res += valueDict[s[i]]

        return res