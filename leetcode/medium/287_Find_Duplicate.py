from typing import List
# https://www.youtube.com/watch?v=wjYnzkAhcNk

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = 0, 0       # nums in range of 1 - n, inclusive
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        slow2 = 0
        while slow != slow2:
            slow = nums[slow]
            slow2 = nums[slow2]

        return slow

