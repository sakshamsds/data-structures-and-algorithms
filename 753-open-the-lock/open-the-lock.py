class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        prohibited = set(deadends)
        visited = set(['0000'])
        q = collections.deque(['0000'])

        if '0000' in prohibited:
            return -1

        def getNbrs(cur_state):
            nbrs = []
            for i in range(4):
                for increment, nxt, set_value in [(1, 10, 0), (-1, -1, 9)]:
                    nxt_digit = int(cur_state[i]) + increment
                    if nxt_digit == nxt:
                        nxt_digit = set_value
                    nbr_state = cur_state.copy()
                    nbr_state[i] = str(nxt_digit)
                    nbrs.append(''.join(nbr_state))
            return nbrs

        min_turns = 0
        while q:
            num_nbrs = len(q)
            for _ in range(num_nbrs):
                cur = q.popleft()
                if cur == target:
                    return min_turns

                nbrs = getNbrs(list(cur))           # create and iterate neighbors
                for nbr in nbrs:
                    if nbr not in prohibited and nbr not in visited:
                        q.append(nbr)
                        visited.add(nbr)
            min_turns += 1

        return -1