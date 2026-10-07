class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        
        def getKey(s):
            freqs = [0] * 26
            for c in s:
                freqs[ord(c) - ord('a')] += 1
            return tuple(freqs)

        groups = collections.defaultdict(list)     # key -> list of word

        for word in strs:
            groups[getKey(word)].append(word)

        return [word for word in groups.values()]