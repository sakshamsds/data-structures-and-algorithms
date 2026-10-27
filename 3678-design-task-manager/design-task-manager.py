class TaskManager:

    def __init__(self, tasks: List[List[int]]):
        # t -> p
        # t -> u
        # (-p, -t)
        self.taskPriorityMap = {}
        self.taskUserMap = {}
        self.min_heap = []
        for userId, taskId, priority in tasks:
            self.add(userId, taskId, priority)

    def add(self, userId: int, taskId: int, priority: int) -> None:
        self.taskPriorityMap[taskId] = priority
        self.taskUserMap[taskId] = userId
        heapq.heappush(self.min_heap, (-priority, -taskId))

    def edit(self, taskId: int, newPriority: int) -> None:
        self.taskPriorityMap[taskId] = newPriority
        heapq.heappush(self.min_heap, (-newPriority, -taskId))

    def rmv(self, taskId: int) -> None: 
        self.taskPriorityMap.pop(taskId)
        self.taskUserMap.pop(taskId)

    def execTop(self) -> int:       # lazy deletions
        while self.min_heap:
            priority, taskId = heapq.heappop(self.min_heap)        
            priority, taskId = -priority, -taskId
            if taskId in self.taskPriorityMap and self.taskPriorityMap[taskId] == priority:      # hasn't been updated
                user = self.taskUserMap[taskId]
                self.rmv(taskId)
                return user
        return -1


# Your TaskManager object will be instantiated and called as such:
# obj = TaskManager(tasks)
# obj.add(userId,taskId,priority)
# obj.edit(taskId,newPriority)
# obj.rmv(taskId)
# param_4 = obj.execTop()