class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_idx = [-1] * 26
        for i, c in enumerate(s):
            last_idx[ord(c) - ord('a')] = i

        sizes = []
        max_idx, start = -1, 0
        for i, c in enumerate(s):
            max_idx = max(max_idx, last_idx[ord(c) - ord('a')])            

            if i == max_idx:
                sizes.append(max_idx - start + 1)
                start = i + 1

        return sizes
