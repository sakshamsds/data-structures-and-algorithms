class Solution:
    def minJumps(self, nums: List[int]) -> int:
        idx_map = collections.defaultdict(list)
        for i, num in enumerate(nums):
            idx_map[num].append(i)

        # bfs        
        visited = set([0])
        q = collections.deque([0])
        min_jumps = 0

        while q:
            level_size = len(q)
            for _ in range(level_size):
                i = q.popleft()
                if i == len(nums) - 1:
                    return min_jumps

                for nbr in idx_map[nums[i]] + [i - 1, i + 1]:
                    if nbr not in visited and nbr >= 0 and nbr < len(nums):
                        q.append(nbr)
                        visited.add(nbr)
                idx_map[nums[i]].clear()        # clear this level

            min_jumps += 1

        return -1
            