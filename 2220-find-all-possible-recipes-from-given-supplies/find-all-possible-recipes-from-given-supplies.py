class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        adj_list = collections.defaultdict(list)
        indegrees = {}
        for i in range(len(ingredients)):
            for ingredient in ingredients[i]:
                adj_list[ingredient].append(recipes[i])
                indegrees[recipes[i]] = 1 + indegrees.get(recipes[i], 0)
                if ingredient not in indegrees:
                    indegrees[ingredient] = 0

        # print(adj_list)
        # print(indegrees)

        q = collections.deque()
        for item, indegree in indegrees.items():
            if indegree == 0:
                q.append(item)

        can_create = []
        while q:
            cur = q.popleft()
            if cur in recipes:
                can_create.append(cur)

            if cur not in supplies and cur not in recipes:
                continue
            
            for ingredient in adj_list[cur]:
                indegrees[ingredient] -= 1
                if indegrees[ingredient] == 0:
                    q.append(ingredient)

        return can_create



