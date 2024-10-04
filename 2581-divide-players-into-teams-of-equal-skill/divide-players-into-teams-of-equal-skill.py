class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        total = sum(skill) * 2 // len(skill)
        freqs = defaultdict(int)

        chemistry = 0
        for s in skill:
            if freqs[total - s] > 0:
                chemistry += s * (total - s)
                freqs[total - s] -= 1
            else:
                freqs[s] += 1

        return chemistry if sum(freqs.values()) == 0 else -1
        
            