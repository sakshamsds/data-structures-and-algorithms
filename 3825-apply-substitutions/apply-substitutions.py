class Solution:
    def applySubstitutions(self, replacements: List[List[str]], text: str) -> str:
        replacement_store = dict()
        for key, value in replacements:
            replacement_store[key] = value

        def dfs(key):
            value = replacement_store[key]
            if '%' not in value:
                return value
            new_value = []
            i = 0
            while i < len(value):
                c = value[i]
                if c != '%':
                    new_value.append(c)
                    i += 1
                else:
                    new_value.append(dfs(value[i + 1]))
                    i += 3
            replacement_store[key] = ''.join(new_value)
            return replacement_store[key]
                    
        # resolve replacements
        for key, value in replacements:
            dfs(key)
        
        res = []
        for pattern in text.split('_'):
            key = pattern[1]
            res.append(replacement_store[key])

        return '_'.join(res)
