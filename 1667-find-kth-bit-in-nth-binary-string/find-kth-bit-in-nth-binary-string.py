class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        seq = "0"
        for i in range(n - 1):
            if k < len(seq):
                return seq[k - 1]
            seq = seq +  "1" + "".join([str(1 ^ int(bit)) for bit in seq][::-1])
        return seq[k - 1]