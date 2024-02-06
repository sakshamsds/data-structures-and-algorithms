class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # key -> [anagrams]
        anagrams = collections.defaultdict(list)
        for s in strs:
            anagrams[tuple(sorted(s))].append(s)
        return anagrams.values()
            

