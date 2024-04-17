class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        
        def dfs(node, cur):
            if not node:
                return 
            cur = chr(ord('a') + node.val) + cur
            if not node.left and not node.right:
                return cur
            left_str = dfs(node.left, cur) if node.left else None
            right_str = dfs(node.right, cur) if node.right else None
            if left_str and right_str:
                return min(left_str, right_str)
            elif left_str:
                return left_str
            else:
                return right_str

        return dfs(root, '')
