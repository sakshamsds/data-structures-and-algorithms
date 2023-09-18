class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:    
        n = len(candidates)   
        res = []
        def backtrack(start, cur_sum, comb):
            if cur_sum > target:
                return
            if cur_sum == target:
                res.append(comb.copy())
                return
            
            for i in range(start, n):
                comb.append(candidates[i])
                backtrack(i, cur_sum + candidates[i], comb)
                comb.pop()

        backtrack(0, 0, [])
        return res
