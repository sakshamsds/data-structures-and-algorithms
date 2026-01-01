# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        ans = []

        def dfs(node):
            if node is None:
                ans.append(1001)
                return

            ans.append(node.val)
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        # print(','.join(map(str, ans)))
        return ','.join(map(str, ans))

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        ans = iter(map(int, data.split(',')))

        def dfs():
            cur = next(ans)
            if cur == 1001:
                return
            node = TreeNode(cur)
            node.left = dfs()
            node.right = dfs()
            return node

        return dfs()
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))