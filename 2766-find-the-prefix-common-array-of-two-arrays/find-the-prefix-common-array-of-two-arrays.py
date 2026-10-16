class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        # previous = set()
        # A[i] in previous, cnt += 1
        # A[]
        # 6,

        # 2 * i - uniques

        n = len(A)
        res = []
        uniques = set()
        for i in range(n):
            uniques.add(A[i])
            uniques.add(B[i])
            res.append(2 * (i + 1) - len(uniques))

        return res