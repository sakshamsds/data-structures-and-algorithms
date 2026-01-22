class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        diff = [gas[i] - cost[i] for i in range(len(gas))]
        if sum(diff) < 0:
            return -1

        start, total = 0, 0
        for i, d in enumerate(diff):
            total += d
            if total < 0:
                total = 0
                start = i + 1

        return start