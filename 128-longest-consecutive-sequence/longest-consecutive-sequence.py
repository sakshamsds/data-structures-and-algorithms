class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        # for every number check if n - 1 is present in the store
        # if not then that is the first element of the sequence
        longest = 0

        for num in nums:
            if num - 1 not in nums:    # start of sequence
                cur_len, cur = 0, num
                while cur in nums:
                    cur_len += 1
                    cur  = cur + 1
                longest = max(cur_len, longest)

        return longest
        
