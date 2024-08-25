class Solution:
    def countPairs(self, nums: List[int]) -> int:

        def compare(n1, n2):
            for i in range(len(n1)):
                for j in range(i + 1, len(n1)):
                    n1[i], n1[j] = n1[j], n1[i]     # swap l and m chars
                    if n1 == n2:    # check
                        return 1
                    n1[i], n1[j] = n1[j], n1[i]     # revert
            return 0

        res = 0
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                num1, num2 = str(nums[i]), str(nums[j])
                if num1 == num2:
                    res += 1
                    continue

                if len(num1) <= len(num2):
                    num1 = '0' * (len(num2) - len(num1)) + num1
                else:
                    num2 = '0' * (len(num1) - len(num2)) + num2
                num1, num2 = list(num1), list(num2)

                res += compare(num1, num2)
        return res            
                        
