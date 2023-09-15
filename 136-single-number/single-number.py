class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        # if a = b, XOR(a, b) = 0
        # keep XOR, single number will be left at the end
        res = 0
        for num in nums:
            res ^= num
            
        return res