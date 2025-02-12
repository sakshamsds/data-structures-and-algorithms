class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        counter = collections.Counter()
        start = 0
        max_fruits = 1

        for end in range(len(fruits)):
            counter[fruits[end]] += 1

            if len(counter) > 2:
                counter[fruits[start]] -= 1
                if not counter[fruits[start]]:
                    counter.pop(fruits[start])
                start += 1

            max_fruits = max(max_fruits, end - start + 1)
        
        return max_fruits
