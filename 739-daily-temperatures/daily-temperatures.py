class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [(temperatures[0], 0)]      # temp, idx
        answer = [0] * len(temperatures)
        for right in range(1, len(temperatures)):
            temp = temperatures[right]
            while stack and stack[-1][0] < temp:
                _, left = stack.pop()
                answer[left] = right - left
            stack.append((temp, right))
        return answer
