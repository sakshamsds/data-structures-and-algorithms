from typing import List

class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        n = len(nums)
        
        # Use a set to store the binary representation directly
        available = set(nums)
        
        max_num = 2 ** n
        for num in range(max_num):
            binary_str = bin(num)[2:].zfill(n)  # Convert to binary and ensure leading zeros
            if binary_str not in available:
                return binary_str
