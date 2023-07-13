class Solution:
    def smallestNumber(self, num: int) -> int:
        if num == 0:
            return 0

        is_positive = 1 if num > 0 else -1
        num *= is_positive
        nums = []
        while num>0:
            nums.append(num % 10)
            num //= 10

        # if num is negative make it the largest number
        # if num i positive make it the smallest number
        nums.sort(reverse=False)
        # nums.sort(reverse=True if is_positive == 1 else False)
        if is_positive == -1:
            nums.reverse()

        # remove leading zeros
        for i in range(len(nums)):
            if nums[i] == 0:
                continue
            else:
                nums[0], nums[i] = nums[i], nums[0]
                break

        # join the number
        result = 0
        for i in range(len(nums)):
            result = result * 10 + nums[i]

        return result * is_positive

    
print(Solution().smallestNumber(310))
print(Solution().smallestNumber(-7605))
print(Solution().smallestNumber(0))
print(Solution().smallestNumber(5))
print(Solution().smallestNumber(-5))