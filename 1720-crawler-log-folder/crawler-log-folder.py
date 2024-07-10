class Solution:
    def minOperations(self, logs: List[str]) -> int:
        subLevel = 0    # 0 identifies main folder
        for log in logs:
            if log == '../' and subLevel > 0:
                    subLevel -= 1
            if log[0] != '.':   # goes into a sub folder
                subLevel += 1
        return subLevel                

                 
