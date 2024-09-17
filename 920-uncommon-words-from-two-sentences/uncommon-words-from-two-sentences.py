class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        cnt = collections.Counter(s1.split() + s2.split())
        res = []
        for k, v in cnt.items():
            if v == 1:
                res.append(k)
        return res