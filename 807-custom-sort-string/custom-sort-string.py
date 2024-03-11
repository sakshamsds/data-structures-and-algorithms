class Solution:
    def customSortString(self, order: str, s: str) -> str:
        freqs = defaultdict(int)
        res = []
        for char in s:
            if char not in order:
                res.append(char)
            else:
                freqs[char] += 1
        for char in order:
            res.extend([char * freqs[char]])
        return ''.join(res)