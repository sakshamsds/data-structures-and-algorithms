class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        cache = {}

        def dfs(i, ones, zeros):
            if i == len(strs):
                return 0

            if (i, ones, zeros) in cache:
                return cache[(i, ones, zeros)]
            
            # do not include cur str
            max_size = dfs(i + 1, ones, zeros)

            # include cur str
            n_ones = ones + strs[i].count('1')
            n_zeros = zeros + strs[i].count('0')
            if n_ones <= n and n_zeros <= m:
                max_size = max(max_size, 1 + dfs(i + 1, n_ones, n_zeros))

            cache[(i, ones, zeros)] = max_size
            return max_size

        return dfs(0, 0, 0)


