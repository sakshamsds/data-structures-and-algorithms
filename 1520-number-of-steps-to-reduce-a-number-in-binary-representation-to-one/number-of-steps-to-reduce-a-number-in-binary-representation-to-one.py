'''
    1101    -> 13
    1110    -> 14
    0111    ->  7
    1000    ->  8
    0100    ->  4
    0010    ->  2
    0001    ->  1

    11001000010000
    1111
'''

class Solution:
    def numSteps(self, s: str) -> int:
        digits = [int(c) for c in s]
        r = len(digits) - 1
        
        def addOne():
            carry = 1
            for k in range(r, -1, -1):
                digit = digits[k]
                digits[k] = (digit + carry) % 2
                carry = (digit + carry) // 2
                if carry == 0:
                    break

        ops = 0
        while r > 0:
            # print(digits, r, ops)
            if digits[r]:  # divide by 2
                addOne()
            else:
                r -= 1
            ops += 1

        return ops if digits[0] else ops + 1

        


        

        