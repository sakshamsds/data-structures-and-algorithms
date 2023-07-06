class Solution:
    # def findTheWinner(self, n: int, k: int) -> int:
    #     # recursive solution
    #     nums = [i for i in range(1, n+1)]

    #     def recursive_jp(cur_pos, nums):
    #         size = len(nums)
    #         if size == 1:
    #             return nums[0]
    #         else:
    #             # remove element at k'th position and recursively call
    #             rm_idx = (cur_pos + k - 1) % size
    #             nums.pop(rm_idx)
    #             return recursive_jp(rm_idx, nums)

    #     return recursive_jp(0, nums)
    
    # # https://leetcode.com/problems/find-the-winner-of-the-circular-game/solutions/2847011/python-code-with-intuition-o-n/
    # yt -> Josephus Problem | GeeksforGeeks
    # W(n, k) -> (W(n-1, k) + k) % n
    def findTheWinner(self, n: int, k: int) -> int:
        return self.helper(n, k) + 1
    
    def helper(self, n, k):
        if n == 1:
            return 0        # winner at index 0
        return (self.helper(n-1, k) + k) % n

    
print(Solution().findTheWinner(7, 3))
print(Solution().findTheWinner(5, 2))
print(Solution().findTheWinner(6, 5))
print(Solution().findTheWinner(1, 1))