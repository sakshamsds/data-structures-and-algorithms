class Solution:
    def numOfPairs(self, nums: List[str], target: str) -> int:
        diffs = collections.defaultdict(int)
        res = 0
        m = len(target)
        for num in nums:
            if num in diffs:
                res += diffs[num]

            n = len(num)
            if n >= m:
                continue

            # add diff
            if num == target[:n]:
                diffs[target[n:]] += 1
            if num == target[m - n:]:
                diffs[target[:m - n]] += 1
            # print(diffs)

        return res