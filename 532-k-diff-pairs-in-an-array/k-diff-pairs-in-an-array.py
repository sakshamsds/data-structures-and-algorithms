class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        res = 0

        if k == 0:  # check repeated numbers, edge case
            counter = Counter(nums)
            for k, v in counter.items():
                if v > 1:
                    res += 1
            return res

        vals = set(nums)
        while vals:
            num = vals.pop()
            left, right = num - k, num + k
            if left in vals:
                res += 1
            if right in vals:
                res += 1 
        return res