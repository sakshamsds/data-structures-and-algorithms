class Solution:
    def minimumPushes(self, word: str) -> int:
        pushes = 0
        freqs = sorted(collections.Counter(word).values(), reverse=True)

        # print(freqs)
        for i, f in enumerate(freqs):
            multiple = i // 8 + 1
            pushes += f * multiple

        return pushes
