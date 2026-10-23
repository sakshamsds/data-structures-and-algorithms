class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # base condition
        if len(s1) > len(s2):
            return False

        s1_freqs = collections.Counter(s1)
        need = len(s1_freqs)

        have = 0
        window_freqs = collections.defaultdict(int)
        for i in range(len(s1) - 1):
            window_freqs[s2[i]] += 1
            if window_freqs[s2[i]] == s1_freqs[s2[i]]:
                have += 1

        l = 0
        for r in range(len(s1) - 1, len(s2)):
            cr = s2[r]
            window_freqs[cr] += 1
            if window_freqs[cr] == s1_freqs[cr]:
                have += 1
            if have == need:
                return True

            cl = s2[l]      # only decrement the value when the freq matches
            if window_freqs[cl] == s1_freqs[cl]:
                have -= 1
            window_freqs[cl] -= 1
            l += 1

        return False
            

