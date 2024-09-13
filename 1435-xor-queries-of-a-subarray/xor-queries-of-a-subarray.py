class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        prefix = []
        p_xor = 0
        for num in arr:
            p_xor ^= num
            prefix.append(p_xor)

        res = []
        for l, r in queries:
            res.append(prefix[r] ^ prefix[l] ^ arr[l])
        return res        