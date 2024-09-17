class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        cnt = collections.Counter(s1.split() + s2.split())
        res = [word for word in cnt if cnt[word] == 1]
        return res