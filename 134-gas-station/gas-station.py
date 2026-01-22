class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        start, prefix, total = 0, 0, 0
        for i in range(len(gas)):
            total += gas[i] - cost[i]
            prefix += gas[i] - cost[i]
            if prefix < 0:
                prefix = 0
                start = i + 1

        return start if total >= 0 else -1