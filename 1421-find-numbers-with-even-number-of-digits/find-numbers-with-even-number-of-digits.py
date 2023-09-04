class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        # convert every number to string an find the length

        # cnt = 0
        # for num in nums:
        #     if len(str(num)) % 2 == 0:
        #         cnt += 1

        # return cnt

        100,000
        # use the constraints
        cnt = 0
        for num in nums:
            if 10 <= num < 100 or 1000 <= num < 10000 or num == 100000:
                cnt += 1

        return cnt