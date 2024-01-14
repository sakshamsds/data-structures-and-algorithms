class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        prev = 0

        for num in arr:
            missing = num - prev - 1
            if k <= missing:
                return prev + k
            k -= missing
            prev = num
        
        return prev + k