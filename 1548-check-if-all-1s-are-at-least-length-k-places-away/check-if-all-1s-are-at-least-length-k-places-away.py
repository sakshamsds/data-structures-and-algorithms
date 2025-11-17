class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        zeros_in_between = k

        for num in nums:
            if num == 0:
                zeros_in_between += 1
                continue

            if zeros_in_between < k:
                return False
            else:
                zeros_in_between = 0

        return True