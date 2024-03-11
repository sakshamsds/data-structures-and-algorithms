class Solution:
    def customSortString(self, order: str, s: str) -> str:
        idxDict = collections.defaultdict(int)
        for i, char in enumerate(order):
            idxDict[char] = i
        return ''.join(sorted(s, key=lambda x : idxDict[x]))
