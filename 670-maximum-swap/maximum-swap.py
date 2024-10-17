'''
2129593
'''

class Solution:
    def maximumSwap(self, num: int) -> int:
        digits = list(str(num))
        suffix_max = [''] * (len(digits) - 1)

        mx = (digits[-1], len(digits) - 1)
        for i in range(len(digits) - 2, -1, -1):
            suffix_max[i] = mx
            if digits[i] > mx[0]:
                mx = (digits[i], i)

        for i in range(len(digits) - 1):
            mx_num, mx_idx = suffix_max[i]
            if mx_num > digits[i]:    # swap and break
                digits[i], digits[mx_idx] = digits[mx_idx], digits[i]
                break

        return int(''.join(digits))


