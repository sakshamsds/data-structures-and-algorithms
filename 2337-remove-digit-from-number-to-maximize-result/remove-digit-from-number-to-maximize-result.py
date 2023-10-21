'''
iterate left to right
next element should be >= digit
if not found remove the last occurence

12131 -> 2131, 1231, 1213 
92939 -> 2939, 9239, 9293
58595 -> 8595, 5895, 5859
'''

class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        size = len(number)
        last_idx = -1
        for i, char in enumerate(number):
            if char == digit:   # check for next element
                last_idx = i
                if i <= size - 2 and number[i+1] > digit:    # next exists?
                    return number[:i] + number[i + 1:]
        
        # if not returned remove the last occurence of char
        return number[:last_idx] + number[last_idx + 1: ]