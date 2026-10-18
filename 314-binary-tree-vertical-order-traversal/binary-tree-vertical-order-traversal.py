# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


'''
			5
		2		6

	1		3		10
				11		12


num_nodes = [0, 100]
node.val = [-100, 100]

vert_pos = [[] for _ in range(201)]

0
.
.	[1,
99	[2,
100	[5, 3
101	[6, 11
102	[10
.	[12, 
.
200

'''

class Solution:
    def verticalOrder(self, root: TreeNode | None) -> list[list[int]]:
        if not root:
            return []
            
        vert_pos = [[] for _ in range(201)]
        
        # level order traversal
        q = deque([(root, 100)])
	
        while q:
            cur, pos = q.popleft()
            vert_pos[pos].append(cur.val)

            if cur.left:
                q.append((cur.left, pos - 1))
            if cur.right:
                q.append((cur.right, pos + 1))

        vertical_order = []
        for row in vert_pos:
            if row:
                vertical_order.append(row)

        return vertical_order

	
