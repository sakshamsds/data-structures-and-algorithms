from typing import List

# https://leetcode.com/problems/convert-the-temperature/

class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        return [celsius + 273.15, celsius*1.80 + 32.00]


inst = Solution()
print(inst.convertTemperature(36.50))
print(inst.convertTemperature(122.11))