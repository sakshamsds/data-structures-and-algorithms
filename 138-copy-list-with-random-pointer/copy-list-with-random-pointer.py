"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None:
            return None

        clones = dict()     # val, Node(val) pairs
        cur = head
        
        # create nodes
        while cur:
            clones[cur] = Node(cur.val)
            cur = cur.next

        cur = head
        while cur:
            if cur.next:
                clones[cur].next = clones[cur.next]
            if cur.random:
                clones[cur].random = clones[cur.random]
            cur = cur.next

        # cur = clones[head]
        # while cur:
            # print(cur.val)
            # cur = cur.next

        # print(clones)
        # for k, v in clones.items():
            # print(v.val, v.next, v.random)
        # return clones[head.val]
        return clones[head]



            
