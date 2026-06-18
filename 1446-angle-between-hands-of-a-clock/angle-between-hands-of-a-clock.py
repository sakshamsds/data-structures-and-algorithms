class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        # 30 - 30/60 * 5 = 27.5
        # 30 - (3 + 30/60) * 5 = 12.5
        # 15 - (3 + 15/60) * 5 = 4/5

        val = abs(minutes - (hour + minutes/60) * 5)
        return min(val, 60 - val) * 6