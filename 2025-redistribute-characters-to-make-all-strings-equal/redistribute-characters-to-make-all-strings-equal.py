class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        # freq of every letter should be a multiple of len of words
        n = len(words)
        freqs = collections.defaultdict(int)

        for word in words:
            for char in word:
                freqs[char] += 1

        for _, freq in freqs.items():
            if freq % n != 0:
                return False

        return True