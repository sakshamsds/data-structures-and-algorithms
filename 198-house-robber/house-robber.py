class Solution:
    def rob(self, nums: List[int]) -> int:
        # we didn't rob the previous house so we rob the current house
        # we robbed the previous hosue so we cannot rob the current house
        no_rob, rob_cur = 0, 0
        
        for num in nums:
            no_rob, rob_cur = max(no_rob, rob_cur), no_rob + num
            
        return max(no_rob, rob_cur)