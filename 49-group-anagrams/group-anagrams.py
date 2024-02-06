class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # key -> [anagrams]
        anagrams = collections.defaultdict(list)

        for s in strs:
            key = [0] * 26
            for c in s:
                key[ord(c) - ord('a')] += 1
            anagrams[tuple(key)].append(s)
        
        return anagrams.values()
            

