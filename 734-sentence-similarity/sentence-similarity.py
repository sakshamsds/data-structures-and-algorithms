class Solution:
    def areSentencesSimilar(self, s1: List[str], s2: List[str], pairs: List[List[str]]) -> bool:
        if len(s1) != len(s2):
            return False

        pairsMap = defaultdict(set)
        for w1, w2 in pairs:
            pairsMap[w1].add(w2)
            pairsMap[w2].add(w1)

        for w1, w2 in zip(s1, s2):
            if w1 == w2 or (w1 in pairsMap and w2 in pairsMap[w1]):
                continue
            else:
                return False

        return True
            
