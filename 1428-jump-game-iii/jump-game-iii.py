class Solution:
    def canReach(self, nums: List[int], start: int) -> bool:
        # bfs
        q = collections.deque()
        q.append(start)
        visited = set([start])

        while q:
            cur_idx = q.popleft()
            if nums[cur_idx] == 0:
                return True
            nbrs = [cur_idx - nums[cur_idx], cur_idx + nums[cur_idx]]
            for nbr in nbrs:
                if nbr not in visited and nbr >= 0 and nbr < len(nums):
                    q.append(nbr)
                    visited.add(nbr)

        return False
        