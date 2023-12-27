class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        res = 0
        for i in range(1, len(colors)):
            if colors[i] == colors[i - 1]:
                # add lower time to res for removal
                res += min(neededTime[i], neededTime[i - 1])  

                # keep the max in the array
                neededTime[i] = max(neededTime[i], neededTime[i - 1])
        return res  

# ab -> 0
# aa -> min(time[0], time[1])
# aaa -> sum(time[0 .. 2]) - max(time[0 .. 2])
# n consecutive -> sum(time[0 .. n - 1]) - max(time[0 .. n - 1]) 
