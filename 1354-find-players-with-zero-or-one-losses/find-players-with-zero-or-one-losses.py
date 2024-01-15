class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        # player -> [wins, losses]
        stats = dict()

        for w, l in matches:
            if w in stats:
                stats[w][0] += 1
            else:
                stats[w] = [1, 0]

            if l in stats:
                stats[l][1] += 1
            else:
                stats[l] = [0, 1]

        # print(stats)
        zero_loss = []
        single_loss = []
        for p, (w, l) in stats.items():
            if l == 0:
                zero_loss.append(p)
            elif l == 1:
                single_loss.append(p)
        
        return [sorted(zero_loss), sorted(single_loss)]
