"""
[[1,1,0,0,0],   -> 2, 0
 [1,1,1,1,0],   -> 4, 1
 [1,0,0,0,0],   -> 1, 2
 [1,1,0,0,0],   -> 2, 3
 [1,1,1,1,1]]   -> 5, 4

calculate # soldiers using binary search
sort and return top k indices
weakest means, min heap with soldiers

"""

class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        m, n = len(mat), len(mat[0])

        def get_soldiers(idx):
            left, right = 0, n
            while left < right:
                mid = left + (right - left) // 2
                if mat[idx][mid] == 0:
                    right = mid
                else:
                    left = mid + 1
            return left

        res = []
        for r in range(m):
            num_sol = get_soldiers(r)
            # print(num_sol)
            res.append((num_sol, r))
        res.sort()
        return [y for x, y in res[0:k]]     
        

    
