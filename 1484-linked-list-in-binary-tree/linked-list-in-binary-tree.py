# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        if not root:
            return False

        if self.isMatching(head, root):
            return True

        return self.isSubPath(head, root.left) or \
                self.isSubPath(head, root.right)


    def isMatching(self, l_node, t_node):
        if not l_node:
            return True

        if not t_node:
            return False

        if l_node.val != t_node.val:
            return False

        return self.isMatching(l_node.next, t_node.left) or \
                self.isMatching(l_node.next, t_node.right)
