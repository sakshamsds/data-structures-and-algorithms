class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        freqs = Counter(arr)    
        
        occurences = set()
        for freq in freqs.values():
            if freq in occurences:
                return False
            occurences.add(freq)

        return True