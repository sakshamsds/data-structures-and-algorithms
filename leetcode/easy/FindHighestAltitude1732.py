"""
https://leetcode.com/problems/find-the-highest-altitude/
1732. Find the Highest Altitude
"""

from typing import List

class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        highest_point = max(0, gain[0])
        for i in range(1, len(gain)):
            gain[i] += gain[i-1]
            highest_point = max(highest_point, gain[i])
        return highest_point
        