class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        maj, freq = 0, 0

        for num in nums:
            if freq == 0:
                maj = num
            if num == maj:
                freq += 1
            else:
                freq -= 1
            # print(maj, freq)

        return maj
        