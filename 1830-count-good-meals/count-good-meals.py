class Solution:
    def countPairs(self, deliciousness: List[int]) -> int:
        two_powers = [2 ** i for i in range(22)]

        MOD = 1_000_000_007
        store = collections.defaultdict(int)

        res = 0
        for d in deliciousness:
            for power in two_powers:
               res = (res + store[power - d]) % MOD
            store[d] += 1 

        return res