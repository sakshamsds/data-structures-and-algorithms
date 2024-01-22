class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        freqs = Counter(nums)
        duplicated = -1
        for k, v in freqs.items():
            if v == 2:
                duplicated = k
                break
        n = len(nums)
        missing = n * (n + 1) // 2 + duplicated - sum(nums)
        return [duplicated, missing]