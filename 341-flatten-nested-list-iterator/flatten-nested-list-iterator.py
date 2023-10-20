# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        # flatten the nested list
        self.idx = -1
        self.flatten = []

        def flatten(nested):
            for element in nested:
                if element.isInteger():
                    self.flatten.append(element.getInteger())
                else:
                    flatten(element.getList())

        flatten(nestedList)
        # print(self.flatten)


    def next(self) -> int:
        self.idx += 1       # next element
        return self.flatten[self.idx]
    
    def hasNext(self) -> bool:
        return self.idx + 1 < len(self.flatten)

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())