class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        def reverse_list(l, r):
            while l < r:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1
            return
        
        n = len(nums)
        k %= n
        
        # reverse nums
        reverse_list(0, n - 1)
        # print(nums)
        
        # reverse first k
        reverse_list(0, k - 1)
        # print(nums)

        # reverse k+1 to last
        reverse_list(k, n - 1)
        # print(nums)
        
        return
        