class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [(temperatures[0], 0)]
        res = [0] * len(temperatures)
        for i in range(1, len(temperatures)):
            cur_temp = temperatures[i]
            while stack and stack[-1][0] < cur_temp:
                _, prev_idx = stack.pop()
                res[prev_idx] = i - prev_idx
            stack.append((cur_temp, i))
        while stack:
            res[stack.pop()[1]] = 0
        return res  