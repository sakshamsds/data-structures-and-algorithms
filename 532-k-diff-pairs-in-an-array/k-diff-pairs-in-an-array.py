class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        res = 0

        if k == 0:  # check repeated numbers
            counter = Counter(nums)
            for k, v in counter.items():
                if v > 1:
                    res += 1
            return res

        vals = set(nums)
        pairs = []
        while vals:
            num = vals.pop()
            left, right = num - k, num + k
            if left in vals:
                pairs.append([num, left])
                res += 1
            if right in vals:
                pairs.append([num, right])
                res += 1 
        return res