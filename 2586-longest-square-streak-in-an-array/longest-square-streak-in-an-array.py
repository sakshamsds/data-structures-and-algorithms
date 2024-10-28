class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        # similar 128. to longest consecutive sequence
        nums = set(nums)
        longest = 0

        for num in nums:
            # if math.sqrt(num) not in nums:  
            cur, length = num, 1
            while cur * cur in nums:
                cur = cur * cur
                length += 1
            longest = max(longest, length)

        return longest if longest >= 2 else -1


