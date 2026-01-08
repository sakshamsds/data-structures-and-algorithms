class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        adj_list = collections.defaultdict(list)
        indegrees = [0] * n
        for prev, nxt in relations:
            prev, nxt = prev - 1, nxt - 1
            indegrees[nxt] += 1
            adj_list[prev].append(nxt)

        q = collections.deque()
        finish_time = [-float(inf)] * n     # course finish time
        for course, indegree in enumerate(indegrees):
            if indegree == 0:
                q.append(course)
                finish_time[course] = time[course]

        while q:
            # print(min_time)
            course = q.popleft()
            for nxt in adj_list[course]:
                indegrees[nxt] -= 1
                finish_time[nxt] = max(finish_time[nxt], finish_time[course] + time[nxt])
                if indegrees[nxt] == 0:
                    q.append(nxt)

        return max(finish_time)