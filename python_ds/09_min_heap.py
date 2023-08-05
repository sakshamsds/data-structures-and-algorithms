import sys

class MinHeap:

    def __init__(self, maxsize):
        self.maxsize = maxsize
        self.size = 0
        self.heap = [0] * (self.maxsize + 1)
        self.heap[0] = -1 * sys.maxsize
        self.front = 1

    # function to return the position of parent for the node currently at pos
    def parent(self, pos):
        return pos//2
    
    # function to return the position of the left child for the node currently at pos
    def left_child(self, pos):
        return 2 * pos
    
    # function to return the position of the right child for the node currently at pos
    def right_child(self, pos):
        return 2 * pos + 1
    
    # function that returns true if the passed node is a leaf node
    def is_leaf(self, pos):
        return 2 * pos > self.size
    
    # function to swap two nodes of the heap
    def swap(self, fpos, spos):
        self.heap[fpos], self.heap[spos] = self.heap[spos], self.heap[fpos]

    # function to heapify the node at pos
    def min_heapify(self, pos):
        # if node is a non-leaf node and greater than any of its child
        if not self.is_leaf(pos):
            if self.heap[pos] > self.heap[self.left_child(pos)] or self.heap[pos] > self.heap[self.right_child(pos)]:

                # swap with the left child and heapify the left child
                if self.heap[self.left_child(pos)] < self.heap[self.right_child(pos)]:
                    self.swap(pos, self.left_child(pos))
                    self.min_heapify(self.left_child(pos))
                else:
                    self.swap(pos, self.right_child(pos))
                    self.min_heapify(self.right_child(pos))

    # function to insert a node into the heap
    def insert(self, element):
        if self.size >= self.maxsize:
            return
        self.size+=1
        self.heap[self.size] = element

        current = self.size

        while self.heap[current] < self.heap[self.parent(current)]:
            self.swap(current, self.parent(current))
            current = self.parent(current)

    # Function to print the contents of the heap
    def print(self):
        for i in range(1, (self.size//2)+1):
            print(" PARENT : "+ str(self.heap[i])+" LEFT CHILD : "+ 
                                str(self.heap[2 * i])+" RIGHT CHILD : "+
                                str(self.heap[2 * i + 1]))    
            
    # function to build the mind heap using the min_heapify function
    def min_heap(self):
        for pos in range(self.size//2, 0, -1):
            self.min_heapify(pos)

    # function to remove and return the minimum element from the heap
    def remove(self):
        popped = self.heap[self.front]
        self.heap[self.front] = self.heap[self.size]
        self.size-=1
        self.min_heapify(self.front)
        return popped
    
# driver code
if __name__ == "__main__":

    min_heap = MinHeap(15)
    min_heap.insert(5)
    min_heap.insert(3)
    min_heap.insert(17)
    min_heap.insert(10)
    min_heap.insert(84)
    min_heap.insert(19)
    min_heap.insert(6)
    min_heap.insert(22)
    min_heap.insert(9)
    min_heap.min_heap()

    min_heap.print()
    print("The Min val is " + str(min_heap.remove()))
