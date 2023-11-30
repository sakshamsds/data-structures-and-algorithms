class Solution:
    def romanToInt(self, s: str) -> int:
        valueDict = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
            'IV': 4,
            'IX': 9,
            'XL': 40,
            'XC': 90,
            'CD': 400,
            'CM': 900
        }
        
        res = 0
        i = 0
        while i < len(s): 
            if (s[i] == 'I' or s[i] == 'X' or s[i] == 'C') and i < len(s) - 1 and s[i:i+2] in valueDict:
                res += valueDict[s[i:i+2]]
                i += 1
            else:
                res += valueDict[s[i]]
            i += 1
        
        return res