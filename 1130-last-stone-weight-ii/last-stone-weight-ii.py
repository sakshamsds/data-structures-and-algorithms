class Solution:
    def lastStoneWeightII(self, stones: list[int]) -> int:
        weights = {0}
        # make two piles
        for stone in stones:
            new_weights = set()
            for w in weights:
                new_weights.add(w + stone)
                new_weights.add(w - stone)
            weights = new_weights

        return min([w if w >= 0 else float('inf') for w in weights])