# Definition for a binary tree node.
import collections
from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        queue = collections.deque()
        queue.appendleft(root)
        while queue:
            num_nodes = len(queue)          # number of nodes at the current level
            temp = []
            for _ in range(num_nodes):
                node = queue.pop()
                if node:
                    temp.append(node.val)
                    queue.appendleft(node.left)
                    queue.appendleft(node.right)

            if temp:
                res.append(temp)
        return res
    
    # def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
    #     if root is None:
    #         return None

    #     res = []
    #     queue = []
    #     queue.insert(0, root)
    #     while queue:
    #         num_nodes = len(queue)          # number of nodes at the current level
    #         temp = []
    #         for _ in range(num_nodes):
    #             node = queue.pop()
    #             temp.append(node.val)
    #             if node.left:
    #                 queue.insert(0, node.left)
    #             if node.right:
    #                 queue.insert(0, node.right)
                
    #         res.append(temp)
    #     return res

