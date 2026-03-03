class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        cache = {0: "0"}

        def dfs(i):
            if i in cache:
                return cache[i]
            prev = dfs(i - 1)
            inverted = ''.join([str(1 ^ int(bit)) for bit in prev])
            cache[i] = prev + "1" + inverted[::-1]
            return cache[i]

        dfs(n)
        # print(cache)
        return cache[n][k-1]
