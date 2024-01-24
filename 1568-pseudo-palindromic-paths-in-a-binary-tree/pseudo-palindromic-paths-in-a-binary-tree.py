# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        freqs = collections.defaultdict(int)
        self.res = 0

        def isPseudoPalindrome():
            odd_freqs = 0
            for val in freqs.values():
                if val % 2 == 1:
                    odd_freqs += 1
                    if odd_freqs > 1:
                        return 0
            return 1

        def dfs(node):
            if not node:
                return 
            freqs[node.val] += 1
            if not node.left and not node.right:        # leaf
                self.res += isPseudoPalindrome()
            dfs(node.left)
            dfs(node.right)
            freqs[node.val] -= 1

        dfs(root)
        return self.res
        