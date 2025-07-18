class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort()
        trainers.sort()
        pi, pairs = 0, 0

        for ti in range(len(trainers)):
            if pi == len(players):
                break

            if players[pi] <= trainers[ti]:
                pairs += 1
                pi += 1

        return pairs                