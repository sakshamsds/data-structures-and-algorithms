class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        # if num - 1 is present, then skip
        # start making the sequence from current element
        store = set(nums)       # for faster lookup

        longest = 0
        for num in store:
            if num - 1 in store:
                continue
            cur = num
            while cur in store:
                cur += 1
            longest = max(longest, cur - num)

        return longest
