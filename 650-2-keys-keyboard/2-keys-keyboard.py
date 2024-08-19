class Solution:
    def minSteps(self, n: int) -> int:

        dp = defaultdict(int)
        
        def dfs(num_As, copied_As):
            if num_As == n:
                return 0

            if num_As + copied_As > n:
                return float('inf')
            
            if (num_As, copied_As) in dp:
                return dp[(num_As, copied_As)]

            if num_As == copied_As:     # paste only
                num_ops = 1 + dfs(num_As + copied_As, copied_As)
                dp[(num_As, copied_As)] = num_ops
                return num_ops

            # copy current_As only when num_As != copied_As
            num_ops = 1 + dfs(num_As, num_As)

            # paste copied_As
            num_ops = min(num_ops, 1 + dfs(num_As + copied_As, copied_As))
            dp[(num_As, copied_As)] = num_ops
            return num_ops

        if n == 1:
            return 0

        return 1 + dfs(1, 1)