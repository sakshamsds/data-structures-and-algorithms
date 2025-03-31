class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        count = collections.Counter(nums)
        for v in count.values():
            if v & 1 == 1:
                return False
        return True