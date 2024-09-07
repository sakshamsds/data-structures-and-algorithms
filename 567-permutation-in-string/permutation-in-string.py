class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        window_size = len(s1)
        need = collections.Counter(s1)

        have = defaultdict(int)
        for r in range(window_size - 1):
            have[s2[r]] += 1

        def isAMatch():     # O(26)
            for c, freq in need.items():
                if have[c] != freq:
                    return False
            return True

        for r in range(window_size - 1, len(s2)):
            have[s2[r]] += 1
            if isAMatch():
                return True
            have[s2[r + 1 - window_size]] -= 1
        return False
