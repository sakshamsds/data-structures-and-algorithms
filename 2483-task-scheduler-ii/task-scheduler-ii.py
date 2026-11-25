class Solution:
    def taskSchedulerII(self, tasks: list[int], space: int) -> int:
        previousDay = {}        # task -> previous day        
        day = 1

        for task in tasks:
            taskPrevDay = previousDay.get(task, -space)
            if day - taskPrevDay <= space:
                day =  taskPrevDay + space + 1
            previousDay[task] = day
            day += 1

        return day - 1