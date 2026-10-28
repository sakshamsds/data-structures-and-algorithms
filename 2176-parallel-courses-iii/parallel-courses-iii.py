class Solution:
    def minimumTime(self, n: int, relations: list[list[int]], time: list[int]) -> int:
        indegrees = [0] * n
        adjList = collections.defaultdict(list)
        for prevC, nextC in relations:
            prevC, nextC = prevC - 1, nextC - 1
            indegrees[nextC] += 1
            adjList[prevC].append(nextC)

        completionTime = [-float('inf')] * n
        q = deque([])
        for i, indegree in enumerate(indegrees):
            if indegree == 0:
                q.append(i)
                completionTime[i] = time[i]

        while q:
            cur = q.popleft()
            for nbr in adjList[cur]:
                completionTime[nbr] = max(completionTime[nbr], completionTime[cur] + time[nbr])
                indegrees[nbr] -= 1
                if indegrees[nbr] == 0:
                    q.append(nbr)

        return max(completionTime)