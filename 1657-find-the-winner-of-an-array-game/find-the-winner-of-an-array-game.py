# no duplicates


class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        q = collections.deque(arr)
        winner = q.popleft()
        new_num = q.popleft()

        num_wins = 0
        prev_winner = -1

        while num_wins < k:
            q.append(min(winner, new_num))     # push min to q before updating winner
            winner = max(winner, new_num)
            # print(q)
            # print(winner)
            if winner == prev_winner:   # greater than all other arra elements
                num_wins += 1
                if num_wins == len(arr) - 1:
                    return winner
            else:
                num_wins = 1
            new_num = q.popleft()
            prev_winner = winner

        return winner