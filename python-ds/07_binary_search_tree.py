"""
Binary Tree and Binary Search Tree

can implement set using binary search tree

binary tree - at max two child nodes

binary search tree - special case of binary tree
    - nodes on left are less that root
    - nodes on right are greater that root
    - no duplicates
    - Search Complexity = O(log n)
    - Insertion Complexity = O(log n)

    - Breadth First Search
    - Depth First Search - where do you put your root node
        - In order traversal: left subtree -> base node -> right subtree                # ascending order
        - Pre order traversal: base node -> left subtree -> right subtree
        - Post order traversal: left subtree -> right subtree -> base node

"""

class BinarySearchTreeNode:
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, data):
        if self.data == data:
            return
        
        if self.data > data:
            # add in left subtree
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinarySearchTreeNode(data)
        else:
            # add in right subtreee
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTreeNode(data)


    def in_order_traversal(self):
        elements = []

        # visit left tree
        if self.left:
            elements += self.left.in_order_traversal()

        # visit base node
        elements.append(self.data)

        # visit right tree
        if self.right:
            elements += self.right.in_order_traversal()
        
        return elements
    
    def search(self, val):
        if self.data == val:
            return True
        
        if val < self.data:
            # val might be in left subtree
            if self.left:
                return self.left.search(val)
            else:
                return False
        else:
            # val might be in right subtree
            if self.right:
                return self.right.search(val)
            else:
                return False
    

def build_tree(elements):
    root = BinarySearchTreeNode(elements[0])

    for i in range(1, len(elements)):
        root.add_child(elements[i])

    return root

if __name__ == '__main__':
    numbers = [17, 4, 1, 20, 9, 23, 18, 24]
    numbers_tree = build_tree(numbers)
    print(numbers_tree.in_order_traversal())            # ascending order
    print(numbers_tree.search(20))
    print(numbers_tree.search(18))
    print(numbers_tree.search(21))