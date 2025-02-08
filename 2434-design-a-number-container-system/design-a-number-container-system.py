class NumberContainers:

    # index -> number
    # number -> heap of indexes

    # lazy approach, resolve the second one during the find operation

    def __init__(self):
        self.idx_to_num = collections.defaultdict(int)
        self.num_to_idxs = collections.defaultdict(list)


    def change(self, index: int, number: int) -> None:  # O(logn)
        # add number to the index
        # add index to heap of indexex for the number
        self.idx_to_num[index] = number
        heapq.heappush(self.num_to_idxs[number], index)


    def find(self, number: int) -> int:
        # the topmost element is not the smallest index
        # verify with index -> number list
        while self.num_to_idxs[number]:
            smallest_idx = self.num_to_idxs[number][0]
            if self.idx_to_num[smallest_idx] == number:
                return smallest_idx
            heapq.heappop(self.num_to_idxs[number])
        return -1
        


# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)