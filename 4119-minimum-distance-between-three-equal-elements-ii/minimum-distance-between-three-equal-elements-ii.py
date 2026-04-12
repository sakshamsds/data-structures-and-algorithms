'''
distance = i, j, k
            (k - i) * 2

    num = [i, j, k, l, m]
'''

class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        idxMap = collections.defaultdict(list)

        for i, num in enumerate(nums):
            idxMap[num].append(i)

        minDistance = 2 * 10 ** 5 + 1
        for _, idxes in idxMap.items():
            if len(idxes) < 3:
                continue
            for i in range(len(idxes) - 2):
                minDistance = min(minDistance, 2 * (idxes[i + 2] - idxes[i]))

        return -1 if minDistance == 2 * 10 ** 5 + 1 else minDistance