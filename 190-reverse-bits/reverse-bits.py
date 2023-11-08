# Input: 1010

#    res<<1             res+=n%2      n>>1
#        00                  00        101
#       000                001          10
#      0010             0010             1
#     00100           00101             _


class Solution:
    def reverseBits(self, n: int) -> int:
        # res = 0
        # for i in range(32):
        #     res = res << 1
        #     bit = n % 2
        #     res += bit
        #     n = n >> 1
        # return res

        res = 0
        for i in range(32):
            bit = (n >> i) & 1
            res += (bit << (31 - i))
        return res
