class Solution:
    def minDeletions(self, s: str) -> int:
        freq_map = collections.defaultdict(int)

        for char in s:
            freq_map[char] += 1

        # print(freq_map)
        seen = set()
        cnt = 0
        for _, freq in freq_map.items():
            while freq in seen:
                freq -= 1
                cnt += 1
            if freq:        # freq not zero
                seen.add(freq)

        return cnt
        