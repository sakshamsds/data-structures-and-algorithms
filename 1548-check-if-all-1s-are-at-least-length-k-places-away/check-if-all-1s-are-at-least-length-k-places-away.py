class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        prev_one = -k - 1
        for i, num in enumerate(nums):
            if num == 1:
                if i - prev_one - 1 < k:
                    return False
                prev_one = i

        return True