class Solution:
    def maxPower(self, s: str) -> int:
        i, power = 0, 0 

        while i < len(s):
            cur_power = 1
            while i + 1 < len(s) and s[i + 1] == s[i]:
                cur_power += 1
                i += 1
            power = max(power, cur_power)
            i += 1

        return power

            