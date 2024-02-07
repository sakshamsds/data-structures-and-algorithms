'''
0 -> 000000000000000000000000
1 -> 000000000000001000000000
2 -> 000000200000001000000000
3 -> 000000300000001000000000

idx1 -> (0, 0), (1, 5), (15, 20)
idx2 -> (snap_shot, value), (snap_shot, value)
'''

class SnapshotArray:

    def __init__(self, length: int):
        self.snap_id = 0
        self.memory = dict()
        for i in range(length):
            self.memory[i] = [(0, 0)] 

    def set(self, index: int, val: int) -> None:
        if self.memory[index][-1][0] == self.snap_id:
            self.memory[index][-1] = (self.snap_id, val)
        else:
            self.memory[index].append((self.snap_id, val))

    def snap(self) -> int:
        self.snap_id += 1
        return self.snap_id - 1

    def get_idx(self, snaps, snap_id):
        l, r = 0, len(snaps) - 1
        while l < r:
            mid = l + (r - l) // 2
            if snaps[mid][0] == snap_id:
                return mid
            elif snaps[mid][0] > snap_id:
                r = mid - 1
            else:
                l = mid + 1
        return l - 1 if snaps[l][0] > snap_id else l

    def get(self, index: int, snap_id: int) -> int:
        # print(self.memory)
        idx = self.get_idx(self.memory[index], snap_id)
        return self.memory[index][idx][1]


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)