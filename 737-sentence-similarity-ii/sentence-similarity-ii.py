class Solution:
    def areSentencesSimilarTwo(self, s1: List[str], s2: List[str], pairs: List[List[str]]) -> bool:
        if len(s1) != len(s2):
            return False
        
        parent = {}     # initial parent is the word itself
        rank = {}       # initial rank is 1 for every word

        for w1, w2 in zip(s1, s2):
            parent[w1], rank[w1] = w1, 1
            parent[w2], rank[w2] = w2, 1

        for w1, w2 in pairs:
            parent[w1], rank[w1] = w1, 1
            parent[w2], rank[w2] = w2, 1

        def find(word):     # O(1)
            if parent[word] != word:
                parent[word] = find(parent[parent[word]])
            return parent[word]

        def union(w1, w2):      # O(1)
            p1, p2 = find(w1), find(w2)
            if p1 == p2:
                return
            if rank[p1] >= rank[p2]:
                parent[p2] = p1
                rank[p1] += rank[p2]
            else:
                parent[p1] = p2
                rank[p2] += rank[p1] 

        for w1, w2 in pairs:        # O(E)
            union(w1, w2)

        for w1, w2 in zip(s1, s2):
            p1, p2 = find(w1), find(w2)
            if p1 != p2:
                return False

        return True

        