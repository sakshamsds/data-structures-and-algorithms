'''
    a   b   b
    # whatever is the larger value, select that more times for now
    aa b aa 
    big, small
    2b1s, 2b1s, 2b1s    
'''

class Solution:
    def strWithout3a3b(self, a: int, b: int) -> str:
        if a > b:
            bigFreq, smallFreq = a, b
            bigVal, smallVal = 'a', 'b'
        else:
            bigFreq, smallFreq = b, a
            bigVal, smallVal = 'b', 'a'

        res = []
        while bigFreq > 0 and smallFreq > 0:
            if bigFreq - smallFreq > 2:
                res.append(bigVal * 2 + smallVal)
                bigFreq -= 1
            else:
                res.append(bigVal + smallVal)
            bigFreq -= 1
            smallFreq -= 1
        
        if bigFreq > 0:
            res.append(bigVal * bigFreq)

        return ''.join(res)