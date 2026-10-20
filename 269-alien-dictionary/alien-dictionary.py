class Solution:
    def alienOrder(self, words: list[str]) -> str:
        adjList = {c : set() for word in words for c in word}

        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            if len(w1) > len(w2) and w1[:len(w2)] == w2:
                return ''
            for c1, c2 in zip(w1, w2):
                if c1 != c2:
                    adjList[c1].add(c2)
                    break

        indegree = {k : 0 for k in adjList.keys()}
        for v in adjList.values():
            for c in v:
                indegree[c] += 1
        # print(indegree)

        q = deque()
        for k, v in indegree.items():
            if v == 0:
                q.append(k)
        # print(q)

        res = []
        while q:
            cur = q.popleft()
            res.append(cur)
            for nbr in adjList[cur]:
                indegree[nbr] -= 1
                if indegree[nbr] == 0:
                    q.append(nbr)

        print(res)
        return '' if sum(indegree.values()) != 0 else ''.join(res)
            