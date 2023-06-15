
# Linked List - Data Structures & Algorithms Tutorials in Python #4

'''
Problem with arrays
    - insertion is O(n)
    - contiguous memory

elements linked with a reference

insertion at beginning = O(1)
deleteion at beginning = O(1)
insert/delete element at the end = O(n)

Advantages
    - No need to pre allocate space
    - insertion is easier
    
'''

class Node:
    def __init__(self, data=None, next=None) -> None:
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self) -> None:
        self.head = None

    def insert_at_beginning(self, data):
        node = Node(data, self.head)            # next will be the current head
        self.head = node

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)        # next is None
            return
        
        itr = self.head
        while itr.next:
            itr = itr.next

        itr.next = Node(data, None)

    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)

    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            itr = itr.next
            count+=1
        return count

    def remove_at(self, index):
        if index < 0 or index >= self.get_length():
            raise Exception("Invalid index")
        
        if index==0:
            self.head = self.head.next              # python does garbage automatically collection unlike C++
            return
        
        count = 0
        itr = self.head
        while itr:
            if count == index-1:
                itr.next = itr.next.next
                break

            itr = itr.next
            count+=1

    def insert_at(self, index, data):
        if index<0 or  index>self.get_length():
            raise Exception("Invalid index")
        
        if index==0:
            self.insert_at_beginning(data)
            return
        
        count=0
        itr = self.head
        while itr:
            if count == index - 1:
                itr.next = Node(data, itr.next)
                break

            itr = itr.next
            count+=1

    def print(self):
        if self.head is None:
            print("Linked list is empty")
            return
        
        itr = self.head
        llstr = ''
        while itr:
            llstr += str(itr.data) + ' --> '
            itr = itr.next

        print(llstr)

    def insert_after_value(self, data_after, data_to_insert):
        # Search for first occurance of data_after value in linked list
        # Now insert data_to_insert after data_after node
        itr = self.head

        while itr:
            if itr.data == data_after:
                itr.next = Node(data_to_insert, itr.next)
                break
            itr = itr.next

    def remove_by_value(self, data):
        # Remove first node that contains data
        if self.head.data == data:
            self.head = self.head.next
        
        itr = self.head

        while itr:
            if itr.next and itr.next.data == data:
                itr.next = itr.next.next
                break
            itr = itr.next
        

if __name__ == '__main__':
    # ll = LinkedList()
    # ll.insert_at_beginning(5)
    # ll.insert_at_beginning(89)
    # ll.insert_at_end(79)
    # ll.insert_at_end(1)
    # ll.insert_values(['banana', 'mango', 'grapes', 'orange'])
    # print(ll.get_length())
    # ll.remove_at(2)
    # ll.insert_at(0, "figs")
    # ll.insert_at(2, "guava")
    # ll.print()
    ll = LinkedList()
    ll.insert_values(["banana","mango","grapes","orange"])
    ll.print()
    ll.insert_after_value("mango","apple") # insert apple after mango
    ll.print()
    ll.remove_by_value("orange") # remove orange from linked list
    ll.print()
    ll.remove_by_value("figs")
    ll.print()
    ll.remove_by_value("banana")
    ll.remove_by_value("mango")
    ll.remove_by_value("apple")
    ll.remove_by_value("grapes")
    ll.print()