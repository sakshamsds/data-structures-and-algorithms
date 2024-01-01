class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        freqs = [0] * 2001
        # -1000 -> 0
        # 0 -> 1000
        # 1000 -> 2001

        for num in arr:
            freqs[num + 1000] += 1

        unique = set()
        for freq in freqs:
            if freq != 0 and freq in unique:
                return False
            unique.add(freq)

        return True