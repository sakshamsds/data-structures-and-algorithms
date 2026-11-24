class Solution:
    def stoneGameIII(self, stones: list[int]) -> str:
        numStones = len(stones)

        cache = {}      # i -> alice score - bob score
        def dfs(i):
            if i >= numStones:
                return 0
            
            if i in cache:
                return cache[i]
            
            # take 1
            score = stones[i] - dfs(i + 1)

            # take 2
            if i < numStones - 1:
                score = max(score, stones[i] + stones[i + 1] - dfs(i + 2))

            # take 3
            if i < numStones - 2:
                score = max(
                    score, 
                    stones[i] + stones[i + 1] + stones[i + 2] - dfs(i + 3)
                )

            cache[i] = score
            return score

        res = dfs(0)
        if res == 0:
            return "Tie"
        if res > 0:
            return "Alice"
        return "Bob"