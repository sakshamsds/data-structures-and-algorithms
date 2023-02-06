# https://leetcode.com/problems/fizz-buzz/
# 412. Fizz Buzz

from typing import List


class Solution:
    def fizzBuzz(self, n: int) -> List[str]:

        output = []

        for i in range(n):
            idx = i + 1

            if idx % 3 == 0:
                if idx % 5 == 0:
                    output.append("FizzBuzz")
                else:
                    output.append("Fizz")
            elif idx % 5 == 0:
                output.append("Buzz")
            else:
                output.append(str(idx))

        return output

print(Solution().fizzBuzz(12))
