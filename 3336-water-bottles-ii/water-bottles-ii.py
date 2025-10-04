class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        drank = numBottles

        while numBottles >= numExchange:
            numBottles -= (numExchange - 1)
            numExchange += 1
            drank += 1

        return drank