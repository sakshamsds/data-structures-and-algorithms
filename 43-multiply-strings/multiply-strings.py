"""
    123 * 6 = 837   =   738
    123 * 5 =  516  =  6150
    123 * 4 =   294 = 49200

"""

class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == '0' or num2 == '0':
            return '0'

        N = len(num1) + len(num2)
        res = [0] * N

        for i, d2 in enumerate(num2[::-1]):
            for j, d1 in enumerate(num1[::-1]):
                pdt = int(d1) * int(d2) + res[i + j]
                res[i + j] = pdt % 10
                res[i + j + 1] += pdt // 10

        for i in range(N - 1, -1, -1):
            if res[i] != 0:
                return "".join([str(d) for d in res[:i + 1][::-1]])

        return "-1"              